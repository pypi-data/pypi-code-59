from pangeamt_nlp.translation_model.translation_model_factory import (
    TranslationModelFactory,
)
import logging
from pangeamt_nlp.seg import Seg
from nteu_translation_engine.pipeline import Pipeline
from typing import Dict, List
from prettytable.prettytable import PLAIN_COLUMNS, _get_size


class Engine:
    def __init__(self, config: Dict, log_file: str = None, dbug: bool = False):
        self._logging = log_file is not None
        if self._logging:
            self._lvl = logging.DEBUG if dbug else logging.INFO
            logging.basicConfig(
                handlers=[logging.FileHandler(log_file)],
                level=self._lvl,
                format="%(asctime)s :: %(levelname)s :: %(message)s"
            )
            self._logger = logging.getLogger("my_logger")
        else:
            self._logger = None
        self._config = config
        self._model = self.load_model()
        self._pipeline = Pipeline(config, self._logger)

    def log(self, message: str, level: str = logging.INFO):
        if self._logging:
            self._logger.log(level, message)

    def load_model(self):
        name = self._config["translation_model"]["name"]
        args = self._config["translation_model"]["args_decoding"]
        if self._config["translation_engine_server"]["gpu"]:
            args["gpu"] = 0
        model_path = self._config["translation_engine_server"]["model_path"]
        self.log(f"Loading -> {name} with arguments {args}.")
        translation_model = TranslationModelFactory.get_class(name)
        return translation_model(model_path, **args)

    async def translate(self, srcs: List):
        translations = self._model.translate(srcs)
        result = []
        for translation in translations:
            if self._lvl == logging.DEBUG:
                n_best = len(translation)
                log_msg = (
                    f"For sentence {translation.pred_sents[0].src_raw}",
                    f"{n_best}-best translations:"
                )
                self.log(log_msg, level=logging.DEBUG)
                f = "\nOption #{0} with score {1}:\n{2}\nAttention:\n"
                for i, prediction in enumerate(translation.pred_sents):
                    log_msg = f.format(
                        i,
                        prediction.score,
                        prediction.sentence
                    )
                    table = prediction.get_pretty_attention()
                    if table is not None:
                        table_fields = table._field_names
                        table_width = len(table_fields)
                        for column_index in range(0, table_width, 3):
                            f_index = column_index
                            l_index = min([column_index + 3, table_width])
                            fields_to_take = table_fields[f_index:l_index]
                            str_to_add = table.get_string(
                                fields=fields_to_take
                            ) + "\n"
                            log_msg += str_to_add
                    self.log(log_msg, level=logging.DEBUG)
            result.append(translation.pred_sents[0].sentence)
        return result

    async def process_batch(self, batch: List, lock=None):
        srcs = []
        segs = []
        ans = []
        for src in batch:
            seg = Seg(src)
            await self._pipeline.preprocess(seg)
            srcs.append(seg.src)
            segs.append(seg)
        if lock is not None:
            async with lock:
                translations = await self.translate(srcs)
        else:
            translations = await self.translate(srcs)
        for translation, seg in zip(translations, segs):
            seg.tgt = seg.tgt_raw = translation
            await self._pipeline.postprocess(seg)
            ans.append(seg.tgt)
            self.log(
                f"Translated -> {seg.src_raw} -> {seg.src} "
                f"-> {seg.tgt_raw} -> {seg.tgt}"
            )
        return ans
