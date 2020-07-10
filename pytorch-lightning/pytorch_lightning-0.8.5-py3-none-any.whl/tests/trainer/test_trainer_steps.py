from pytorch_lightning import Trainer
from tests.base.deterministic_model import DeterministicModel
import pytest
import torch


@pytest.mark.skipif(torch.cuda.device_count() < 2, reason="test requires multi-GPU machine")
def test_training_step_dict(tmpdir):
    """
    Tests that only training_step can be used
    """
    model = DeterministicModel()
    model.training_step = model.training_step_dict_return
    model.val_dataloader = None

    trainer = Trainer(
        default_root_dir=tmpdir,
        fast_dev_run=True,
        weights_summary=None,
    )
    trainer.fit(model)

    # make sure correct steps were called
    assert model.training_step_called
    assert not model.training_step_end_called
    assert not model.training_epoch_end_called

    # make sure training outputs what is expected
    for batch_idx, batch in enumerate(model.train_dataloader()):
        break

    out = trainer.run_training_batch(batch, batch_idx)
    assert out.signal == 0
    assert out.batch_log_metrics['log_acc1'] == 12.0
    assert out.batch_log_metrics['log_acc2'] == 7.0

    train_step_out = out.training_step_output_for_epoch_end
    pbar_metrics = train_step_out['progress_bar']
    assert 'log' in train_step_out
    assert 'progress_bar' in train_step_out
    assert train_step_out['train_step_test'] == 549
    assert pbar_metrics['pbar_acc1'] == 17.0
    assert pbar_metrics['pbar_acc2'] == 19.0

    # make sure the optimizer closure returns the correct things
    opt_closure_result = trainer.optimizer_closure(batch, batch_idx, 0, trainer.optimizers[0], trainer.hiddens)
    assert opt_closure_result['loss'] == (42.0 * 3) + (15.0 * 3)


def training_step_with_step_end(tmpdir):
    """
    Checks train_step + training_step_end
    """
    model = DeterministicModel()
    model.training_step = model.training_step_for_step_end_dict
    model.training_step_end = model.training_step_end_dict
    model.val_dataloader = None

    trainer = Trainer(fast_dev_run=True, weights_summary=None)
    trainer.fit(model)

    # make sure correct steps were called
    assert model.training_step_called
    assert model.training_step_end_called
    assert not model.training_epoch_end_called

    # make sure training outputs what is expected
    for batch_idx, batch in enumerate(model.train_dataloader()):
        break

    out = trainer.run_training_batch(batch, batch_idx)
    assert out.signal == 0
    assert out.batch_log_metrics['log_acc1'] == 14.0
    assert out.batch_log_metrics['log_acc2'] == 9.0

    train_step_end_out = out.training_step_output_for_epoch_end
    pbar_metrics = train_step_end_out['progress_bar']
    assert 'train_step_end' in train_step_end_out
    assert pbar_metrics['pbar_acc1'] == 19.0
    assert pbar_metrics['pbar_acc2'] == 21.0


def test_full_training_loop_dict(tmpdir):
    """
    Checks train_step + training_step_end + training_epoch_end
    """
    model = DeterministicModel()
    model.training_step = model.training_step_for_step_end_dict
    model.training_step_end = model.training_step_end_dict
    model.training_epoch_end = model.training_epoch_end_dict
    model.val_dataloader = None

    trainer = Trainer(
        default_root_dir=tmpdir,
        max_epochs=1,
        weights_summary=None,
    )
    trainer.fit(model)

    # make sure correct steps were called
    assert model.training_step_called
    assert model.training_step_end_called
    assert model.training_epoch_end_called

    # assert epoch end metrics were added
    assert trainer.callback_metrics['epoch_end_log_1'] == 178
    assert trainer.progress_bar_metrics['epoch_end_pbar_1'] == 234

    # make sure training outputs what is expected
    for batch_idx, batch in enumerate(model.train_dataloader()):
        break

    out = trainer.run_training_batch(batch, batch_idx)
    assert out.signal == 0
    assert out.batch_log_metrics['log_acc1'] == 14.0
    assert out.batch_log_metrics['log_acc2'] == 9.0

    train_step_end_out = out.training_step_output_for_epoch_end
    pbar_metrics = train_step_end_out['progress_bar']
    assert pbar_metrics['pbar_acc1'] == 19.0
    assert pbar_metrics['pbar_acc2'] == 21.0


def test_train_step_epoch_end(tmpdir):
    """
    Checks train_step + training_epoch_end (NO training_step_end)
    """
    model = DeterministicModel()
    model.training_step = model.training_step_dict_return
    model.training_step_end = None
    model.training_epoch_end = model.training_epoch_end_dict
    model.val_dataloader = None

    trainer = Trainer(max_epochs=1, weights_summary=None)
    trainer.fit(model)

    # make sure correct steps were called
    assert model.training_step_called
    assert not model.training_step_end_called
    assert model.training_epoch_end_called

    # assert epoch end metrics were added
    assert trainer.callback_metrics['epoch_end_log_1'] == 178
    assert trainer.progress_bar_metrics['epoch_end_pbar_1'] == 234

    # make sure training outputs what is expected
    for batch_idx, batch in enumerate(model.train_dataloader()):
        break

    out = trainer.run_training_batch(batch, batch_idx)
    assert out.signal == 0
    assert out.batch_log_metrics['log_acc1'] == 12.0
    assert out.batch_log_metrics['log_acc2'] == 7.0

    train_step_end_out = out.training_step_output_for_epoch_end
    pbar_metrics = train_step_end_out['progress_bar']
    assert pbar_metrics['pbar_acc1'] == 17.0
    assert pbar_metrics['pbar_acc2'] == 19.0
