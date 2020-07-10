# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tencentcloud.common.abstract_model import AbstractModel


class AddDelayLiveStreamRequest(AbstractModel):
    """AddDelayLiveStream request structure.

    """

    def __init__(self):
        """
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        :param DomainName: Push domain name.
        :type DomainName: str
        :param StreamName: Stream name.
        :type StreamName: str
        :param DelayTime: Delay time in seconds, up to 600s.
        :type DelayTime: int
        :param ExpireTime: Expiration time of the configured delayed playback in UTC format, such as 2018-11-29T19:00:00Z.
Notes:
1. The configuration will expire after 7 days by default and can last up to 7 days.
2. The Beijing time is in UTC+8. This value should be in the format as required by ISO 8601. For more information, please see [ISO Date and Time Format](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type ExpireTime: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None
        self.DelayTime = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        self.DelayTime = params.get("DelayTime")
        self.ExpireTime = params.get("ExpireTime")


class AddDelayLiveStreamResponse(AbstractModel):
    """AddDelayLiveStream response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddLiveDomainRequest(AbstractModel):
    """AddLiveDomain request structure.

    """

    def __init__(self):
        """
        :param DomainName: Domain name.
        :type DomainName: str
        :param DomainType: Domain name type.
0: push domain name.
1: playback domain name.
        :type DomainType: int
        :param PlayType: Pull domain name type:
1: Mainland China.
2: global.
3: outside Mainland China.
Default value: 1.
        :type PlayType: int
        :param IsDelayLive: Whether it is LCB:
0: LVB,
1: LCB.
Default value: 0.
        :type IsDelayLive: int
        :param IsMiniProgramLive: Whether it is LVB on Mini Program.
0: LVB.
1: LVB on Mini Program.
Default value: 0.
        :type IsMiniProgramLive: int
        """
        self.DomainName = None
        self.DomainType = None
        self.PlayType = None
        self.IsDelayLive = None
        self.IsMiniProgramLive = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.DomainType = params.get("DomainType")
        self.PlayType = params.get("PlayType")
        self.IsDelayLive = params.get("IsDelayLive")
        self.IsMiniProgramLive = params.get("IsMiniProgramLive")


class AddLiveDomainResponse(AbstractModel):
    """AddLiveDomain response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddLiveWatermarkRequest(AbstractModel):
    """AddLiveWatermark request structure.

    """

    def __init__(self):
        """
        :param PictureUrl: Watermark image URL.
        :type PictureUrl: str
        :param WatermarkName: Watermark name.
        :type WatermarkName: str
        :param XPosition: Display position: X-axis offset. Default value: 0.
        :type XPosition: int
        :param YPosition: Display position: Y-axis offset. Default value: 0.
        :type YPosition: int
        :param Width: Watermark width or its percentage of the live streaming video width. It is recommended to just specify either height or width as the other will be scaled proportionally to avoid distortions. The original width is used by default.
        :type Width: int
        :param Height: Watermark height or its percentage of the live streaming video width. It is recommended to just specify either height or width as the other will be scaled proportionally to avoid distortions. The original height is used by default.
        :type Height: int
        """
        self.PictureUrl = None
        self.WatermarkName = None
        self.XPosition = None
        self.YPosition = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.PictureUrl = params.get("PictureUrl")
        self.WatermarkName = params.get("WatermarkName")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class AddLiveWatermarkResponse(AbstractModel):
    """AddLiveWatermark response structure.

    """

    def __init__(self):
        """
        :param WatermarkId: Watermark ID.
        :type WatermarkId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.WatermarkId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        self.RequestId = params.get("RequestId")


class BillDataInfo(AbstractModel):
    """Bandwidth and traffic information.

    """

    def __init__(self):
        """
        :param Time: Time point in the format of `yyyy-mm-dd HH:MM:SS`.
        :type Time: str
        :param Bandwidth: Bandwidth in Mbps.
        :type Bandwidth: float
        :param Flux: Traffic in MB.
        :type Flux: float
        :param PeakTime: Time point of peak value in the format of `yyyy-mm-dd HH:MM:SS`. As raw data is at a 5-minute granularity, if data at a 1-hour or 1-day granularity is queried, the time point of peak bandwidth value at the corresponding granularity will be returned.
        :type PeakTime: str
        """
        self.Time = None
        self.Bandwidth = None
        self.Flux = None
        self.PeakTime = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Bandwidth = params.get("Bandwidth")
        self.Flux = params.get("Flux")
        self.PeakTime = params.get("PeakTime")


class BindLiveDomainCertRequest(AbstractModel):
    """BindLiveDomainCert request structure.

    """

    def __init__(self):
        """
        :param CertId: Certificate ID, which can be obtained through the `CreateLiveCert` API.
        :type CertId: int
        :param DomainName: Playback domain name.
        :type DomainName: str
        :param Status: Status. 0: off, 1: on.
        :type Status: int
        """
        self.CertId = None
        self.DomainName = None
        self.Status = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.DomainName = params.get("DomainName")
        self.Status = params.get("Status")


class BindLiveDomainCertResponse(AbstractModel):
    """BindLiveDomainCert response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CallBackRuleInfo(AbstractModel):
    """Rule information

    """

    def __init__(self):
        """
        :param CreateTime: Rule creation time.
        :type CreateTime: str
        :param UpdateTime: Rule update time.
        :type UpdateTime: str
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param DomainName: Push domain name.
        :type DomainName: str
        :param AppName: Push path.
        :type AppName: str
        """
        self.CreateTime = None
        self.UpdateTime = None
        self.TemplateId = None
        self.DomainName = None
        self.AppName = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.TemplateId = params.get("TemplateId")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")


class CallBackTemplateInfo(AbstractModel):
    """Callback template information.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param TemplateName: Template name.
        :type TemplateName: str
        :param Description: Description.
        :type Description: str
        :param StreamBeginNotifyUrl: Stream starting callback URL.
        :type StreamBeginNotifyUrl: str
        :param StreamEndNotifyUrl: Interruption callback URL.
        :type StreamEndNotifyUrl: str
        :param StreamMixNotifyUrl: Stream mixing callback URL.
        :type StreamMixNotifyUrl: str
        :param RecordNotifyUrl: Recording callback URL.
        :type RecordNotifyUrl: str
        :param SnapshotNotifyUrl: Screencapturing callback URL.
        :type SnapshotNotifyUrl: str
        :param PornCensorshipNotifyUrl: Porn detection callback URL.
        :type PornCensorshipNotifyUrl: str
        :param CallbackKey: Callback authentication key.
        :type CallbackKey: str
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.StreamBeginNotifyUrl = None
        self.StreamEndNotifyUrl = None
        self.StreamMixNotifyUrl = None
        self.RecordNotifyUrl = None
        self.SnapshotNotifyUrl = None
        self.PornCensorshipNotifyUrl = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.StreamBeginNotifyUrl = params.get("StreamBeginNotifyUrl")
        self.StreamEndNotifyUrl = params.get("StreamEndNotifyUrl")
        self.StreamMixNotifyUrl = params.get("StreamMixNotifyUrl")
        self.RecordNotifyUrl = params.get("RecordNotifyUrl")
        self.SnapshotNotifyUrl = params.get("SnapshotNotifyUrl")
        self.PornCensorshipNotifyUrl = params.get("PornCensorshipNotifyUrl")
        self.CallbackKey = params.get("CallbackKey")


class CancelCommonMixStreamRequest(AbstractModel):
    """CancelCommonMixStream request structure.

    """

    def __init__(self):
        """
        :param MixStreamSessionId: ID of stream mix session (from applying for stream mix to canceling stream mix).
        :type MixStreamSessionId: str
        """
        self.MixStreamSessionId = None


    def _deserialize(self, params):
        self.MixStreamSessionId = params.get("MixStreamSessionId")


class CancelCommonMixStreamResponse(AbstractModel):
    """CancelCommonMixStream response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CdnPlayStatData(AbstractModel):
    """Downstream playback statistical metrics

    """

    def __init__(self):
        """
        :param Time: Time point in the format of `yyyy-mm-dd HH:MM:SS`.
        :type Time: str
        :param Bandwidth: Bandwidth in Mbps.
        :type Bandwidth: float
        :param Flux: Traffic in MB.
        :type Flux: float
        :param Request: Number of new requests.
        :type Request: int
        :param Online: Number of concurrent connections.
        :type Online: int
        """
        self.Time = None
        self.Bandwidth = None
        self.Flux = None
        self.Request = None
        self.Online = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Bandwidth = params.get("Bandwidth")
        self.Flux = params.get("Flux")
        self.Request = params.get("Request")
        self.Online = params.get("Online")


class CertInfo(AbstractModel):
    """Certificate information.

    """

    def __init__(self):
        """
        :param CertId: Certificate ID.
        :type CertId: int
        :param CertName: Certificate name.
        :type CertName: str
        :param Description: Description.
        :type Description: str
        :param CreateTime: Creation time in UTC format.
        :type CreateTime: str
        :param HttpsCrt: Certificate content.
        :type HttpsCrt: str
        :param CertType: Certificate type:
0: Tencent Cloud-hosted certificate.
1: user-added certificate.
        :type CertType: int
        :param CertExpireTime: Certificate expiration time in UTC format.
        :type CertExpireTime: str
        :param DomainList: List of domain names that use this certificate.
        :type DomainList: list of str
        """
        self.CertId = None
        self.CertName = None
        self.Description = None
        self.CreateTime = None
        self.HttpsCrt = None
        self.CertType = None
        self.CertExpireTime = None
        self.DomainList = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.CertName = params.get("CertName")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.HttpsCrt = params.get("HttpsCrt")
        self.CertType = params.get("CertType")
        self.CertExpireTime = params.get("CertExpireTime")
        self.DomainList = params.get("DomainList")


class CommonMixControlParams(AbstractModel):
    """General stream mix control parameter

    """

    def __init__(self):
        """
        :param UseMixCropCenter: Valid values: [0,1].
If 1 is entered, when the layer resolution in the parameter is different from the actual video resolution, the video will be automatically cropped according to the resolution set by the layer.
        :type UseMixCropCenter: int
        """
        self.UseMixCropCenter = None


    def _deserialize(self, params):
        self.UseMixCropCenter = params.get("UseMixCropCenter")


class CommonMixCropParams(AbstractModel):
    """General stream mix input crop parameter.

    """

    def __init__(self):
        """
        :param CropWidth: Crop width. Value range: [0,2000].
        :type CropWidth: float
        :param CropHeight: Crop height. Value range: [0,2000].
        :type CropHeight: float
        :param CropStartLocationX: Starting crop X coordinate. Value range: [0,2000].
        :type CropStartLocationX: float
        :param CropStartLocationY: Starting crop Y coordinate. Value range: [0,2000].
        :type CropStartLocationY: float
        """
        self.CropWidth = None
        self.CropHeight = None
        self.CropStartLocationX = None
        self.CropStartLocationY = None


    def _deserialize(self, params):
        self.CropWidth = params.get("CropWidth")
        self.CropHeight = params.get("CropHeight")
        self.CropStartLocationX = params.get("CropStartLocationX")
        self.CropStartLocationY = params.get("CropStartLocationY")


class CommonMixInputParam(AbstractModel):
    """General stream mix input parameter.

    """

    def __init__(self):
        """
        :param InputStreamName: Input stream name of up to 80 bytes, which is a string containing letters, digits, and underscores.
        :type InputStreamName: str
        :param LayoutParams: Input stream layout parameter.
        :type LayoutParams: :class:`tencentcloud.live.v20180801.models.CommonMixLayoutParams`
        :param CropParams: Input stream crop parameter.
        :type CropParams: :class:`tencentcloud.live.v20180801.models.CommonMixCropParams`
        """
        self.InputStreamName = None
        self.LayoutParams = None
        self.CropParams = None


    def _deserialize(self, params):
        self.InputStreamName = params.get("InputStreamName")
        if params.get("LayoutParams") is not None:
            self.LayoutParams = CommonMixLayoutParams()
            self.LayoutParams._deserialize(params.get("LayoutParams"))
        if params.get("CropParams") is not None:
            self.CropParams = CommonMixCropParams()
            self.CropParams._deserialize(params.get("CropParams"))


class CommonMixLayoutParams(AbstractModel):
    """General stream mix layout parameter.

    """

    def __init__(self):
        """
        :param ImageLayer: Input layer. Value range: [1,16].
1) For `image_layer` of background stream (i.e., main host video image or canvas), enter 1.
2) For audio stream mix, this parameter is also required.
        :type ImageLayer: int
        :param InputType: Input type. Value range: [0,5].
If this parameter is left empty, 0 will be used by default.
0: the input stream is audio/video.
2: the input stream is image.
3: the input stream is canvas. 
4: the input stream is audio.
5: the input stream is pure video.
        :type InputType: int
        :param ImageWidth: Output width of input video image. Value range:
Pixel: [0,2000]
Percentage: [0.01,0.99]
If this parameter is left empty, the input stream width will be used by default.
If percentage is used, the expected output is (percentage * background width).
        :type ImageWidth: float
        :param ImageHeight: Output height of input video image. Value range:
Pixel: [0,2000]
Percentage: [0.01,0.99]
If this parameter is left empty, the input stream height will be used by default.
If percentage is used, the expected output is (percentage * background height).
        :type ImageHeight: float
        :param LocationX: X-axis offset of input in output video image. Value range:
Pixel: [0,2000]
Percentage: [0.01,0.99]
If this parameter is left empty, 0 will be used by default.
Horizontal offset from the top-left corner of main host background video image. 
If percentage is used, the expected output is (percentage * background width).
        :type LocationX: float
        :param LocationY: Y-axis offset of input in output video image. Value range:
Pixel: [0,2000]
Percentage: [0.01,0.99]
If this parameter is left empty, 0 will be used by default.
Vertical offset from the top-left corner of main host background video image. 
If percentage is used, the expected output is (percentage * background width)
        :type LocationY: float
        :param Color: When `InputType` is 3 (canvas), this value indicates the canvas color.
Commonly used colors include:
Red: 0xcc0033.
Yellow: 0xcc9900.
Green: 0xcccc33.
Blue: 0x99CCFF.
Black: 0x000000.
White: 0xFFFFFF.
Gray: 0x999999
        :type Color: str
        :param WatermarkId: When `InputType` is 2 (image), this value is the watermark ID.
        :type WatermarkId: int
        """
        self.ImageLayer = None
        self.InputType = None
        self.ImageWidth = None
        self.ImageHeight = None
        self.LocationX = None
        self.LocationY = None
        self.Color = None
        self.WatermarkId = None


    def _deserialize(self, params):
        self.ImageLayer = params.get("ImageLayer")
        self.InputType = params.get("InputType")
        self.ImageWidth = params.get("ImageWidth")
        self.ImageHeight = params.get("ImageHeight")
        self.LocationX = params.get("LocationX")
        self.LocationY = params.get("LocationY")
        self.Color = params.get("Color")
        self.WatermarkId = params.get("WatermarkId")


class CommonMixOutputParams(AbstractModel):
    """General stream mix output parameter.

    """

    def __init__(self):
        """
        :param OutputStreamName: Output stream name.
        :type OutputStreamName: str
        :param OutputStreamType: Output stream type. Valid values: [0,1].
If this parameter is left empty, 0 will be used by default.
If the output stream is a stream in the input stream list, enter 0.
If you want the stream mix result to be a new stream, enter 1.
If this value is 1, `output_stream_id` cannot appear in `input_stram_list`, and there cannot be a stream with the same ID on the LVB backend.
        :type OutputStreamType: int
        :param OutputStreamBitRate: Output stream bitrate. Value range: [1,50000].
If this parameter is left empty, the system will automatically determine.
        :type OutputStreamBitRate: int
        :param OutputStreamGop: Output stream GOP size. Value range: [1,10].
If this parameter is left empty, the system will automatically determine.
        :type OutputStreamGop: int
        :param OutputStreamFrameRate: Output stream frame rate. Value range: [1,60].
If this parameter is left empty, the system will automatically determine.
        :type OutputStreamFrameRate: int
        :param OutputAudioBitRate: Output stream audio bitrate. Value range: [1,500]
If this parameter is left empty, the system will automatically determine.
        :type OutputAudioBitRate: int
        :param OutputAudioSampleRate: Output stream audio sample rate. Valid values: [96000, 88200, 64000, 48000, 44100, 32000,24000, 22050, 16000, 12000, 11025, 8000].
If this parameter is left empty, the system will automatically determine.
        :type OutputAudioSampleRate: int
        :param OutputAudioChannels: Output stream audio sound channel. Valid values: [1,2].
If this parameter is left empty, the system will automatically determine.
        :type OutputAudioChannels: int
        :param MixSei: SEI information in output stream. If there are no special needs, leave it empty.
        :type MixSei: str
        """
        self.OutputStreamName = None
        self.OutputStreamType = None
        self.OutputStreamBitRate = None
        self.OutputStreamGop = None
        self.OutputStreamFrameRate = None
        self.OutputAudioBitRate = None
        self.OutputAudioSampleRate = None
        self.OutputAudioChannels = None
        self.MixSei = None


    def _deserialize(self, params):
        self.OutputStreamName = params.get("OutputStreamName")
        self.OutputStreamType = params.get("OutputStreamType")
        self.OutputStreamBitRate = params.get("OutputStreamBitRate")
        self.OutputStreamGop = params.get("OutputStreamGop")
        self.OutputStreamFrameRate = params.get("OutputStreamFrameRate")
        self.OutputAudioBitRate = params.get("OutputAudioBitRate")
        self.OutputAudioSampleRate = params.get("OutputAudioSampleRate")
        self.OutputAudioChannels = params.get("OutputAudioChannels")
        self.MixSei = params.get("MixSei")


class ConcurrentRecordStreamNum(AbstractModel):
    """Number of concurrent recording channels

    """

    def __init__(self):
        """
        :param Time: Time point.
        :type Time: str
        :param Num: Number of channels.
        :type Num: int
        """
        self.Time = None
        self.Num = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Num = params.get("Num")


class CreateCommonMixStreamRequest(AbstractModel):
    """CreateCommonMixStream request structure.

    """

    def __init__(self):
        """
        :param MixStreamSessionId: ID of stream mix session (from applying for stream mix to canceling stream mix).
        :type MixStreamSessionId: str
        :param InputStreamList: Input stream list for stream mix.
        :type InputStreamList: list of CommonMixInputParam
        :param OutputParams: Output stream parameter for stream mix.
        :type OutputParams: :class:`tencentcloud.live.v20180801.models.CommonMixOutputParams`
        :param MixStreamTemplateId: Input template ID. If this parameter is set, the output will be generated according to the default template layout, and there is no need to enter the custom position parameters.
If this parameter is left empty, 0 will be used by default.
For two input sources, 10, 20, 30, 40, and 50 are supported.
For three input sources, 310, 390, and 391 are supported.
For four input sources, 410 is supported.
For five input sources, 510 and 590 are supported.
For six input sources, 610 is supported.
        :type MixStreamTemplateId: int
        :param ControlParams: Special control parameter for stream mix. If there are no special needs, leave it empty.
        :type ControlParams: :class:`tencentcloud.live.v20180801.models.CommonMixControlParams`
        """
        self.MixStreamSessionId = None
        self.InputStreamList = None
        self.OutputParams = None
        self.MixStreamTemplateId = None
        self.ControlParams = None


    def _deserialize(self, params):
        self.MixStreamSessionId = params.get("MixStreamSessionId")
        if params.get("InputStreamList") is not None:
            self.InputStreamList = []
            for item in params.get("InputStreamList"):
                obj = CommonMixInputParam()
                obj._deserialize(item)
                self.InputStreamList.append(obj)
        if params.get("OutputParams") is not None:
            self.OutputParams = CommonMixOutputParams()
            self.OutputParams._deserialize(params.get("OutputParams"))
        self.MixStreamTemplateId = params.get("MixStreamTemplateId")
        if params.get("ControlParams") is not None:
            self.ControlParams = CommonMixControlParams()
            self.ControlParams._deserialize(params.get("ControlParams"))


class CreateCommonMixStreamResponse(AbstractModel):
    """CreateCommonMixStream response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLiveCallbackRuleRequest(AbstractModel):
    """CreateLiveCallbackRule request structure.

    """

    def __init__(self):
        """
        :param DomainName: Push domain name.
        :type DomainName: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        :param TemplateId: Template ID.
        :type TemplateId: int
        """
        self.DomainName = None
        self.AppName = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.TemplateId = params.get("TemplateId")


class CreateLiveCallbackRuleResponse(AbstractModel):
    """CreateLiveCallbackRule response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLiveCallbackTemplateRequest(AbstractModel):
    """CreateLiveCallbackTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateName: Template name.
Maximum length: 255 bytes.
Only letters, digits, underscores, and hyphens can be contained.
        :type TemplateName: str
        :param Description: Description.
Maximum length: 1,024 bytes.
Only letters, digits, underscores, and hyphens can be contained.
        :type Description: str
        :param StreamBeginNotifyUrl: Stream starting callback URL,
Protocol document: [Event Message Notification](/document/product/267/32744).
        :type StreamBeginNotifyUrl: str
        :param StreamEndNotifyUrl: Interruption callback URL,
Protocol document: [Event Message Notification](/document/product/267/32744).
        :type StreamEndNotifyUrl: str
        :param RecordNotifyUrl: Recording callback URL,
Protocol document: [Event Message Notification](/document/product/267/32744).
        :type RecordNotifyUrl: str
        :param SnapshotNotifyUrl: Screencapturing callback URL,
Protocol document: [Event Message Notification](/document/product/267/32744).
        :type SnapshotNotifyUrl: str
        :param PornCensorshipNotifyUrl: Porn detection callback URL,
Protocol document: [Event Message Notification](/document/product/267/32741).
        :type PornCensorshipNotifyUrl: str
        :param CallbackKey: Callback key. The callback URL is public. For the callback signature, please see the event message notification document.
[Event Message Notification](/document/product/267/32744).
        :type CallbackKey: str
        """
        self.TemplateName = None
        self.Description = None
        self.StreamBeginNotifyUrl = None
        self.StreamEndNotifyUrl = None
        self.RecordNotifyUrl = None
        self.SnapshotNotifyUrl = None
        self.PornCensorshipNotifyUrl = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.StreamBeginNotifyUrl = params.get("StreamBeginNotifyUrl")
        self.StreamEndNotifyUrl = params.get("StreamEndNotifyUrl")
        self.RecordNotifyUrl = params.get("RecordNotifyUrl")
        self.SnapshotNotifyUrl = params.get("SnapshotNotifyUrl")
        self.PornCensorshipNotifyUrl = params.get("PornCensorshipNotifyUrl")
        self.CallbackKey = params.get("CallbackKey")


class CreateLiveCallbackTemplateResponse(AbstractModel):
    """CreateLiveCallbackTemplate response structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class CreateLiveCertRequest(AbstractModel):
    """CreateLiveCert request structure.

    """

    def __init__(self):
        """
        :param CertType: Certificate type. 0: user-added certificate, 1: Tencent Cloud-hosted certificate.
Note: if the certificate type is 0, `HttpsCrt` and `HttpsKey` are required;
If the certificate type is 1, the certificate corresponding to `CloudCertId` will be used first. If `CloudCertId` is empty, `HttpsCrt` and `HttpsKey` will be used.
        :type CertType: int
        :param CertName: Certificate name.
        :type CertName: str
        :param HttpsCrt: Certificate content, i.e., public key.
        :type HttpsCrt: str
        :param HttpsKey: Private key.
        :type HttpsKey: str
        :param Description: Description.
        :type Description: str
        :param CloudCertId: Tencent Cloud-hosted certificate ID.
        :type CloudCertId: str
        """
        self.CertType = None
        self.CertName = None
        self.HttpsCrt = None
        self.HttpsKey = None
        self.Description = None
        self.CloudCertId = None


    def _deserialize(self, params):
        self.CertType = params.get("CertType")
        self.CertName = params.get("CertName")
        self.HttpsCrt = params.get("HttpsCrt")
        self.HttpsKey = params.get("HttpsKey")
        self.Description = params.get("Description")
        self.CloudCertId = params.get("CloudCertId")


class CreateLiveCertResponse(AbstractModel):
    """CreateLiveCert response structure.

    """

    def __init__(self):
        """
        :param CertId: Certificate ID
        :type CertId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CertId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.RequestId = params.get("RequestId")


class CreateLiveRecordRequest(AbstractModel):
    """CreateLiveRecord request structure.

    """

    def __init__(self):
        """
        :param StreamName: Stream name.
        :type StreamName: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        :param DomainName: Push domain name. This parameter must be set for multi-domain name push.
        :type DomainName: str
        :param StartTime: Recording start time, which is China standard time and should be URL-encoded (RFC3986). For example, the encoding of 2017-01-01 10:10:01 is 2017-01-01+10%3a10%3a01.
In scheduled recording mode, this field must be set; in real-time video recording mode, this field is ignored.
        :type StartTime: str
        :param EndTime: Recording end time, which is China standard time and should be URL-encoded (RFC3986). For example, the encoding of 2017-01-01 10:30:01 is 2017-01-01+10%3a30%3a01.
In scheduled recording mode, this field must be set; in real-time video recording mode, this field is optional. If the recording is set to real-time video recording mode through the `Highlight` parameter, the set end time should not be more than 30 minutes after the current time. If the set end time is more than 30 minutes after the current time, earlier than the current time, or left empty, the actual end time will be 30 minutes after the current time.
        :type EndTime: str
        :param RecordType: Recording type.
"video": Audio-video recording **(default)**.
"audio": audio recording.
In both scheduled and real-time video recording modes, this parameter is valid and is not case sensitive.
        :type RecordType: str
        :param FileFormat: Recording file format. Valid values:
"flv" **(default)**, "hls", "mp4", "aac", "mp3".
In both scheduled and real-time video recording modes, this parameter is valid and is not case sensitive.
        :type FileFormat: str
        :param Highlight: Mark for enabling real-time video recording mode.
0: Real-time video recording mode is not enabled, i.e., the scheduled recording mode is used **(default)**. See [Sample 1](#.E7.A4.BA.E4.BE.8B1-.E5.88.9B.E5.BB.BA.E5.AE.9A.E6.97.B6.E5.BD.95.E5.88.B6.E4.BB.BB.E5.8A.A1).
1: Real-time video recording mode is enabled. See [Sample 2](#.E7.A4.BA.E4.BE.8B2-.E5.88.9B.E5.BB.BA.E5.AE.9E.E6.97.B6.E5.BD.95.E5.88.B6.E4.BB.BB.E5.8A.A1).
        :type Highlight: int
        :param MixStream: Flag for enabling A+B=C mixed stream recording.
0: A+B=C mixed stream recording is not enabled **(default)**.
1: A+B=C mixed stream recording is enabled.
In both scheduled and real-time video recording modes, this parameter is valid.
        :type MixStream: int
        :param StreamParam: Recording stream parameter. The following parameters are supported currently:
record_interval: recording interval in seconds. Value range: 1800-7200.
storage_time: recording file storage duration in seconds.
Example: record_interval=3600&storage_time=2592000.
Note: the parameter needs to be URL-encoded.
In both scheduled and real-time video recording modes, this parameter is valid.
        :type StreamParam: str
        """
        self.StreamName = None
        self.AppName = None
        self.DomainName = None
        self.StartTime = None
        self.EndTime = None
        self.RecordType = None
        self.FileFormat = None
        self.Highlight = None
        self.MixStream = None
        self.StreamParam = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RecordType = params.get("RecordType")
        self.FileFormat = params.get("FileFormat")
        self.Highlight = params.get("Highlight")
        self.MixStream = params.get("MixStream")
        self.StreamParam = params.get("StreamParam")


class CreateLiveRecordResponse(AbstractModel):
    """CreateLiveRecord response structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID, which uniquely identifies a recording task globally.
        :type TaskId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateLiveRecordRuleRequest(AbstractModel):
    """CreateLiveRecordRule request structure.

    """

    def __init__(self):
        """
        :param DomainName: Push domain name.
        :type DomainName: str
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.
        :type AppName: str
        :param StreamName: Stream name.
Note: If the parameter is a non-empty string, the rule will be only applicable to the particular stream.
        :type StreamName: str
        """
        self.DomainName = None
        self.TemplateId = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.TemplateId = params.get("TemplateId")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")


class CreateLiveRecordRuleResponse(AbstractModel):
    """CreateLiveRecordRule response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLiveRecordTemplateRequest(AbstractModel):
    """CreateLiveRecordTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateName: Template name. Only letters, digits, underscores, and hyphens can be contained.
        :type TemplateName: str
        :param Description: Message description
        :type Description: str
        :param FlvParam: FLV recording parameter, which is set when FLV recording is enabled.
        :type FlvParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param HlsParam: HLS recording parameter, which is set when HLS recording is enabled.
        :type HlsParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param Mp4Param: Mp4 recording parameter, which is set when Mp4 recording is enabled.
        :type Mp4Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param AacParam: AAC recording parameter, which is set when AAC recording is enabled.
        :type AacParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param IsDelayLive: LVB type. Default value: 0.
0: LVB.
1: LCB.
        :type IsDelayLive: int
        :param HlsSpecialParam: HLS-specific recording parameter.
        :type HlsSpecialParam: :class:`tencentcloud.live.v20180801.models.HlsSpecialParam`
        :param Mp3Param: Mp3 recording parameter, which is set when Mp3 recording is enabled.
        :type Mp3Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        """
        self.TemplateName = None
        self.Description = None
        self.FlvParam = None
        self.HlsParam = None
        self.Mp4Param = None
        self.AacParam = None
        self.IsDelayLive = None
        self.HlsSpecialParam = None
        self.Mp3Param = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        if params.get("FlvParam") is not None:
            self.FlvParam = RecordParam()
            self.FlvParam._deserialize(params.get("FlvParam"))
        if params.get("HlsParam") is not None:
            self.HlsParam = RecordParam()
            self.HlsParam._deserialize(params.get("HlsParam"))
        if params.get("Mp4Param") is not None:
            self.Mp4Param = RecordParam()
            self.Mp4Param._deserialize(params.get("Mp4Param"))
        if params.get("AacParam") is not None:
            self.AacParam = RecordParam()
            self.AacParam._deserialize(params.get("AacParam"))
        self.IsDelayLive = params.get("IsDelayLive")
        if params.get("HlsSpecialParam") is not None:
            self.HlsSpecialParam = HlsSpecialParam()
            self.HlsSpecialParam._deserialize(params.get("HlsSpecialParam"))
        if params.get("Mp3Param") is not None:
            self.Mp3Param = RecordParam()
            self.Mp3Param._deserialize(params.get("Mp3Param"))


class CreateLiveRecordTemplateResponse(AbstractModel):
    """CreateLiveRecordTemplate response structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class CreateLiveSnapshotRuleRequest(AbstractModel):
    """CreateLiveSnapshotRule request structure.

    """

    def __init__(self):
        """
        :param DomainName: Push domain name.
        :type DomainName: str
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        :param StreamName: Stream name.
Note: if this parameter is a non-empty string, the rule will take effect only for the particular stream.
        :type StreamName: str
        """
        self.DomainName = None
        self.TemplateId = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.TemplateId = params.get("TemplateId")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")


class CreateLiveSnapshotRuleResponse(AbstractModel):
    """CreateLiveSnapshotRule response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLiveSnapshotTemplateRequest(AbstractModel):
    """CreateLiveSnapshotTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateName: Template name.
Maximum length: 255 bytes.
Only letters, digits, underscores, and hyphens can be contained.
        :type TemplateName: str
        :param CosAppId: COS application ID.
        :type CosAppId: int
        :param CosBucket: COS bucket name.
        :type CosBucket: str
        :param CosRegion: COS region.
        :type CosRegion: str
        :param Description: Description.
Maximum length: 1,024 bytes.
Only letters, digits, underscores, and hyphens can be contained.
        :type Description: str
        :param SnapshotInterval: Screencapturing interval in seconds. Default value: 10s.
Value range: 5–600s.
        :type SnapshotInterval: int
        :param Width: Screenshot width. Default value: 0 (original width).
        :type Width: int
        :param Height: Screenshot height. Default value: 0 (original height).
        :type Height: int
        :param PornFlag: Whether to enable porn detection. 0: no, 1: yes. Default value: 0
        :type PornFlag: int
        :param CosPrefix: COS bucket folder prefix.
        :type CosPrefix: str
        :param CosFileName: COS filename.
        :type CosFileName: str
        """
        self.TemplateName = None
        self.CosAppId = None
        self.CosBucket = None
        self.CosRegion = None
        self.Description = None
        self.SnapshotInterval = None
        self.Width = None
        self.Height = None
        self.PornFlag = None
        self.CosPrefix = None
        self.CosFileName = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.CosAppId = params.get("CosAppId")
        self.CosBucket = params.get("CosBucket")
        self.CosRegion = params.get("CosRegion")
        self.Description = params.get("Description")
        self.SnapshotInterval = params.get("SnapshotInterval")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.PornFlag = params.get("PornFlag")
        self.CosPrefix = params.get("CosPrefix")
        self.CosFileName = params.get("CosFileName")


class CreateLiveSnapshotTemplateResponse(AbstractModel):
    """CreateLiveSnapshotTemplate response structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class CreateLiveTranscodeRuleRequest(AbstractModel):
    """CreateLiveTranscodeRule request structure.

    """

    def __init__(self):
        """
        :param DomainName: Playback domain name.
        :type DomainName: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default. If you only bind a domain name, leave this parameter empty.
        :type AppName: str
        :param StreamName: Stream name. If only the domain name or path is bound, leave this parameter blank.
        :type StreamName: str
        :param TemplateId: Designates an existing template ID.
        :type TemplateId: int
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.TemplateId = params.get("TemplateId")


class CreateLiveTranscodeRuleResponse(AbstractModel):
    """CreateLiveTranscodeRule response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLiveTranscodeTemplateRequest(AbstractModel):
    """CreateLiveTranscodeTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateName: Template name, such as 900 900p. This can be only a combination of letters and digits.
        :type TemplateName: str
        :param VideoBitrate: Video bitrate. Value range: 100–8,000.
Note: The bitrate must be a multiple of 100.
        :type VideoBitrate: int
        :param Vcodec: Video encoding format. Valid values: h264, h265. Default value: h264.
        :type Vcodec: str
        :param Acodec: Audio encoding in ACC format. Default value: original audio format.
Note: This parameter will take effect later.
        :type Acodec: str
        :param AudioBitrate: Audio bitrate. Value range: 0–500. Default value: 0.
        :type AudioBitrate: int
        :param Description: Template description.
        :type Description: str
        :param Width: Width. Default value: 0.
        :type Width: int
        :param NeedVideo: Whether to keep the video. 0: no; 1: yes. Default value: 1.
        :type NeedVideo: int
        :param NeedAudio: Whether to keep the audio. 0: no; 1: yes. Default value: 1.
        :type NeedAudio: int
        :param Height: Height. Default value: 0.
        :type Height: int
        :param Fps: Frame rate. Default value: 0.
        :type Fps: int
        :param Gop: Keyframe interval in seconds. Original interval by default
        :type Gop: int
        :param Rotate: Whether to rotate. 0: no; 1: yes. Default value: 0.
        :type Rotate: int
        :param Profile: Encoding quality:
baseline/main/high. Default value: baseline.
        :type Profile: str
        :param BitrateToOrig: Whether to not exceed the original bitrate. 0: no; 1: yes. Default value: 0.
        :type BitrateToOrig: int
        :param HeightToOrig: Whether to not exceed the original height. 0: no; 1: yes. Default value: 0.
        :type HeightToOrig: int
        :param FpsToOrig: Whether to not exceed the original frame rate. 0: no; 1: yes. Default value: 0.
        :type FpsToOrig: int
        :param AiTransCode: Whether it is a top speed codec template. 0: no, 1: yes. Default value: 0.
        :type AiTransCode: int
        :param AdaptBitratePercent: `VideoBitrate` minus top speed codec bitrate. Value range: 0.1–0.5.
        :type AdaptBitratePercent: float
        """
        self.TemplateName = None
        self.VideoBitrate = None
        self.Vcodec = None
        self.Acodec = None
        self.AudioBitrate = None
        self.Description = None
        self.Width = None
        self.NeedVideo = None
        self.NeedAudio = None
        self.Height = None
        self.Fps = None
        self.Gop = None
        self.Rotate = None
        self.Profile = None
        self.BitrateToOrig = None
        self.HeightToOrig = None
        self.FpsToOrig = None
        self.AiTransCode = None
        self.AdaptBitratePercent = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.VideoBitrate = params.get("VideoBitrate")
        self.Vcodec = params.get("Vcodec")
        self.Acodec = params.get("Acodec")
        self.AudioBitrate = params.get("AudioBitrate")
        self.Description = params.get("Description")
        self.Width = params.get("Width")
        self.NeedVideo = params.get("NeedVideo")
        self.NeedAudio = params.get("NeedAudio")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        self.Gop = params.get("Gop")
        self.Rotate = params.get("Rotate")
        self.Profile = params.get("Profile")
        self.BitrateToOrig = params.get("BitrateToOrig")
        self.HeightToOrig = params.get("HeightToOrig")
        self.FpsToOrig = params.get("FpsToOrig")
        self.AiTransCode = params.get("AiTransCode")
        self.AdaptBitratePercent = params.get("AdaptBitratePercent")


class CreateLiveTranscodeTemplateResponse(AbstractModel):
    """CreateLiveTranscodeTemplate response structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class CreateLiveWatermarkRuleRequest(AbstractModel):
    """CreateLiveWatermarkRule request structure.

    """

    def __init__(self):
        """
        :param DomainName: Push domain name.
        :type DomainName: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        :param StreamName: Stream name.
        :type StreamName: str
        :param TemplateId: Watermark ID, which is the `WatermarkId` returned by the [AddLiveWatermark](/document/product/267/30154) API.
        :type TemplateId: int
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.TemplateId = params.get("TemplateId")


class CreateLiveWatermarkRuleResponse(AbstractModel):
    """CreateLiveWatermarkRule response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DelayInfo(AbstractModel):
    """Delayed playback information.

    """

    def __init__(self):
        """
        :param DomainName: Push domain name.
        :type DomainName: str
        :param AppName: Push path, which is the same as the 
 `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        :param StreamName: Stream name.
        :type StreamName: str
        :param DelayInterval: Delay time in seconds.
        :type DelayInterval: int
        :param CreateTime: Creation time in UTC time.
Note: the difference between UTC time and Beijing time is 8 hours.
Example: 2019-06-18T12:00:00Z (i.e., June 18, 2019 20:00:00 Beijing time).
        :type CreateTime: str
        :param ExpireTime: Expiration time in UTC time.
Note: the difference between UTC time and Beijing time is 8 hours.
Example: 2019-06-18T12:00:00Z (i.e., June 18, 2019 20:00:00 Beijing time).
        :type ExpireTime: str
        :param Status: Current status:
-1: expired.
1: in effect.
        :type Status: int
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None
        self.DelayInterval = None
        self.CreateTime = None
        self.ExpireTime = None
        self.Status = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.DelayInterval = params.get("DelayInterval")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.Status = params.get("Status")


class DeleteLiveCallbackRuleRequest(AbstractModel):
    """DeleteLiveCallbackRule request structure.

    """

    def __init__(self):
        """
        :param DomainName: Push domain name.
        :type DomainName: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        """
        self.DomainName = None
        self.AppName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")


class DeleteLiveCallbackRuleResponse(AbstractModel):
    """DeleteLiveCallbackRule response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveCallbackTemplateRequest(AbstractModel):
    """DeleteLiveCallbackTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
1. Get the template ID in the returned value of the [CreateLiveCallbackTemplate](/document/product/267/32637) API call.
2. You can query the list of created templates through the [DescribeLiveCallbackTemplates](/document/product/267/32632) API.
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class DeleteLiveCallbackTemplateResponse(AbstractModel):
    """DeleteLiveCallbackTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveCertRequest(AbstractModel):
    """DeleteLiveCert request structure.

    """

    def __init__(self):
        """
        :param CertId: Certificate ID.
        :type CertId: int
        """
        self.CertId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")


class DeleteLiveCertResponse(AbstractModel):
    """DeleteLiveCert response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveDomainRequest(AbstractModel):
    """DeleteLiveDomain request structure.

    """

    def __init__(self):
        """
        :param DomainName: Domain name to be deleted.
        :type DomainName: str
        :param DomainType: Type. 0: push, 1: playback.
        :type DomainType: int
        """
        self.DomainName = None
        self.DomainType = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.DomainType = params.get("DomainType")


class DeleteLiveDomainResponse(AbstractModel):
    """DeleteLiveDomain response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveRecordRequest(AbstractModel):
    """DeleteLiveRecord request structure.

    """

    def __init__(self):
        """
        :param StreamName: Stream name.
        :type StreamName: str
        :param TaskId: Task ID, which uniquely identifies a recording task globally.
Get the `TaskId` from the returned value of the [CreateLiveRecord](/document/product/267/30148) API.
        :type TaskId: int
        """
        self.StreamName = None
        self.TaskId = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.TaskId = params.get("TaskId")


class DeleteLiveRecordResponse(AbstractModel):
    """DeleteLiveRecord response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveRecordRuleRequest(AbstractModel):
    """DeleteLiveRecordRule request structure.

    """

    def __init__(self):
        """
        :param DomainName: Push domain name.
Domain name+AppName+StreamName uniquely identifies a single transcoding rule. If you need to delete it, strong match is required. For example, even if AppName is blank, you need to pass in a blank string to make a strong match.
        :type DomainName: str
        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.
Domain name+AppName+StreamName uniquely identifies a single transcoding rule. If you need to delete it, strong match is required. For example, even if AppName is blank, you need to pass in a blank string to make a strong match.
        :type AppName: str
        :param StreamName: Stream name.
Domain name+AppName+StreamName uniquely identifies a single transcoding rule. If you need to delete it, strong match is required. For example, even if AppName is blank, you need to pass in a blank string to make a strong match.
        :type StreamName: str
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")


class DeleteLiveRecordRuleResponse(AbstractModel):
    """DeleteLiveRecordRule response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveRecordTemplateRequest(AbstractModel):
    """DeleteLiveRecordTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class DeleteLiveRecordTemplateResponse(AbstractModel):
    """DeleteLiveRecordTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveSnapshotRuleRequest(AbstractModel):
    """DeleteLiveSnapshotRule request structure.

    """

    def __init__(self):
        """
        :param DomainName: Push domain name.
        :type DomainName: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        :param StreamName: Stream name.
        :type StreamName: str
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")


class DeleteLiveSnapshotRuleResponse(AbstractModel):
    """DeleteLiveSnapshotRule response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveSnapshotTemplateRequest(AbstractModel):
    """DeleteLiveSnapshotTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
1. Get from the returned value of the [CreateLiveSnapshotTemplate](/document/product/267/32624) API call.
2. You can query the list of created screencapturing templates through the [DescribeLiveSnapshotTemplates](/document/product/267/32619) API.
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class DeleteLiveSnapshotTemplateResponse(AbstractModel):
    """DeleteLiveSnapshotTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveTranscodeRuleRequest(AbstractModel):
    """DeleteLiveTranscodeRule request structure.

    """

    def __init__(self):
        """
        :param DomainName: Playback domain name.
        :type DomainName: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        :param StreamName: Stream name.
        :type StreamName: str
        :param TemplateId: Template ID.
        :type TemplateId: int
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.TemplateId = params.get("TemplateId")


class DeleteLiveTranscodeRuleResponse(AbstractModel):
    """DeleteLiveTranscodeRule response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveTranscodeTemplateRequest(AbstractModel):
    """DeleteLiveTranscodeTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
1. Get the template ID in the returned value of the [CreateLiveTranscodeTemplate](/document/product/267/32646) API call.
2. You can query the list of created templates through the [DescribeLiveTranscodeTemplates](/document/product/267/32641) API.
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class DeleteLiveTranscodeTemplateResponse(AbstractModel):
    """DeleteLiveTranscodeTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveWatermarkRequest(AbstractModel):
    """DeleteLiveWatermark request structure.

    """

    def __init__(self):
        """
        :param WatermarkId: Watermark ID.
Get the watermark ID in the returned value of the [AddLiveWatermark](/document/product/267/30154) API call.
        :type WatermarkId: int
        """
        self.WatermarkId = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")


class DeleteLiveWatermarkResponse(AbstractModel):
    """DeleteLiveWatermark response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveWatermarkRuleRequest(AbstractModel):
    """DeleteLiveWatermarkRule request structure.

    """

    def __init__(self):
        """
        :param DomainName: Push domain name.
        :type DomainName: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        :param StreamName: Stream name.
        :type StreamName: str
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")


class DeleteLiveWatermarkRuleResponse(AbstractModel):
    """DeleteLiveWatermarkRule response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeBillBandwidthAndFluxListRequest(AbstractModel):
    """DescribeBillBandwidthAndFluxList request structure.

    """

    def __init__(self):
        """
        :param StartTime: Start time point in the format of `yyyy-mm-dd HH:MM:SS`.
        :type StartTime: str
        :param EndTime: End time point in the format of `yyyy-mm-dd HH:MM:SS`. The difference between the start time and end time cannot be greater than 31 days.
        :type EndTime: str
        :param PlayDomains: LVB playback domain name. If this parameter is left empty, full data will be queried.
        :type PlayDomains: list of str
        :param MainlandOrOversea: Valid values:
Mainland: query data for Mainland China,
Oversea: query data for regions outside Mainland China,
Default: query data for all regions.
Note: LEB only supports querying data for all regions.
        :type MainlandOrOversea: str
        :param Granularity: Data granularity. Valid values:
5: 5-minute granularity (the query time span should be within 1 day),
60: 1-hour granularity (the query time span should be within one month),
1440: 1-day granularity (the query time span should be within one month).
Default value: 5.
        :type Granularity: int
        :param ServiceName: Service name. Valid values: LVB, LEB. Default value: LVB.
        :type ServiceName: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomains = None
        self.MainlandOrOversea = None
        self.Granularity = None
        self.ServiceName = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomains = params.get("PlayDomains")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.Granularity = params.get("Granularity")
        self.ServiceName = params.get("ServiceName")


class DescribeBillBandwidthAndFluxListResponse(AbstractModel):
    """DescribeBillBandwidthAndFluxList response structure.

    """

    def __init__(self):
        """
        :param PeakBandwidthTime: Time point of peak bandwidth value in the format of `yyyy-mm-dd HH:MM:SS`.
        :type PeakBandwidthTime: str
        :param PeakBandwidth: Peak bandwidth in Mbps.
        :type PeakBandwidth: float
        :param P95PeakBandwidthTime: Time point of 95th percentile bandwidth value in the format of `yyyy-mm-dd HH:MM:SS`.
        :type P95PeakBandwidthTime: str
        :param P95PeakBandwidth: 95th percentile bandwidth in Mbps.
        :type P95PeakBandwidth: float
        :param SumFlux: Total traffic in MB.
        :type SumFlux: float
        :param DataInfoList: Detailed data information.
        :type DataInfoList: list of BillDataInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PeakBandwidthTime = None
        self.PeakBandwidth = None
        self.P95PeakBandwidthTime = None
        self.P95PeakBandwidth = None
        self.SumFlux = None
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PeakBandwidthTime = params.get("PeakBandwidthTime")
        self.PeakBandwidth = params.get("PeakBandwidth")
        self.P95PeakBandwidthTime = params.get("P95PeakBandwidthTime")
        self.P95PeakBandwidth = params.get("P95PeakBandwidth")
        self.SumFlux = params.get("SumFlux")
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = BillDataInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeConcurrentRecordStreamNumRequest(AbstractModel):
    """DescribeConcurrentRecordStreamNum request structure.

    """

    def __init__(self):
        """
        :param LiveType: Live streaming type. SlowLive: LCB.
NormalLive: LVB.
        :type LiveType: str
        :param StartTime: Start time in the format of `yyyy-mm-dd HH:MM:SS`.
Data for the last 180 days can be queried.
        :type StartTime: str
        :param EndTime: End time in the format of `yyyy-mm-dd HH:MM:SS`.
The maximum time span supported is 31 days.
        :type EndTime: str
        :param MainlandOrOversea: Valid values: Mainland (data for Mainland China), Oversea (data for regions outside Mainland China). If this parameter is left empty, data for all regions will be queried.
        :type MainlandOrOversea: str
        :param PushDomains: Playback domain name list. If this parameter is left empty, full data will be queried.
        :type PushDomains: list of str
        """
        self.LiveType = None
        self.StartTime = None
        self.EndTime = None
        self.MainlandOrOversea = None
        self.PushDomains = None


    def _deserialize(self, params):
        self.LiveType = params.get("LiveType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.PushDomains = params.get("PushDomains")


class DescribeConcurrentRecordStreamNumResponse(AbstractModel):
    """DescribeConcurrentRecordStreamNum response structure.

    """

    def __init__(self):
        """
        :param DataInfoList: Statistics list.
        :type DataInfoList: list of ConcurrentRecordStreamNum
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = ConcurrentRecordStreamNum()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGroupProIspPlayInfoListRequest(AbstractModel):
    """DescribeGroupProIspPlayInfoList request structure.

    """

    def __init__(self):
        """
        :param StartTime: Start time point in the format of `yyyy-mm-dd HH:MM:SS`.
        :type StartTime: str
        :param EndTime: End time point in the format of `yyyy-mm-dd HH:MM:SS`
The time span is (0,3 hours]. Data for the last month can be queried.
        :type EndTime: str
        :param PlayDomains: Playback domain name. If this parameter is left empty, full data will be queried.
        :type PlayDomains: list of str
        :param ProvinceNames: District list. If this parameter is left empty, data for all districts will be returned.
        :type ProvinceNames: list of str
        :param IspNames: ISP list. If this parameter is left empty, data of all ISPs will be returned.
        :type IspNames: list of str
        :param MainlandOrOversea: Within or outside Mainland China. Valid values: Mainland (data for Mainland China), Oversea (data for regions outside Mainland China). If this parameter is left empty, data for all regions will be queried.
        :type MainlandOrOversea: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomains = None
        self.ProvinceNames = None
        self.IspNames = None
        self.MainlandOrOversea = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomains = params.get("PlayDomains")
        self.ProvinceNames = params.get("ProvinceNames")
        self.IspNames = params.get("IspNames")
        self.MainlandOrOversea = params.get("MainlandOrOversea")


class DescribeGroupProIspPlayInfoListResponse(AbstractModel):
    """DescribeGroupProIspPlayInfoList response structure.

    """

    def __init__(self):
        """
        :param DataInfoList: Data content.
        :type DataInfoList: list of GroupProIspDataInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = GroupProIspDataInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveCallbackRulesRequest(AbstractModel):
    """DescribeLiveCallbackRules request structure.

    """


class DescribeLiveCallbackRulesResponse(AbstractModel):
    """DescribeLiveCallbackRules response structure.

    """

    def __init__(self):
        """
        :param Rules: Rule information list.
        :type Rules: list of CallBackRuleInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = CallBackRuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveCallbackTemplateRequest(AbstractModel):
    """DescribeLiveCallbackTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
1. Get the template ID in the returned value of the [CreateLiveCallbackTemplate](/document/product/267/32637) API call.
2. You can query the list of created templates through the [DescribeLiveCallbackTemplates](/document/product/267/32632) API.
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class DescribeLiveCallbackTemplateResponse(AbstractModel):
    """DescribeLiveCallbackTemplate response structure.

    """

    def __init__(self):
        """
        :param Template: Callback template information.
        :type Template: :class:`tencentcloud.live.v20180801.models.CallBackTemplateInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = CallBackTemplateInfo()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")


class DescribeLiveCallbackTemplatesRequest(AbstractModel):
    """DescribeLiveCallbackTemplates request structure.

    """


class DescribeLiveCallbackTemplatesResponse(AbstractModel):
    """DescribeLiveCallbackTemplates response structure.

    """

    def __init__(self):
        """
        :param Templates: Template information list.
        :type Templates: list of CallBackTemplateInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Templates = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = CallBackTemplateInfo()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveCertRequest(AbstractModel):
    """DescribeLiveCert request structure.

    """

    def __init__(self):
        """
        :param CertId: Certificate ID.
        :type CertId: int
        """
        self.CertId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")


class DescribeLiveCertResponse(AbstractModel):
    """DescribeLiveCert response structure.

    """

    def __init__(self):
        """
        :param CertInfo: Certificate information.
        :type CertInfo: :class:`tencentcloud.live.v20180801.models.CertInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CertInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CertInfo") is not None:
            self.CertInfo = CertInfo()
            self.CertInfo._deserialize(params.get("CertInfo"))
        self.RequestId = params.get("RequestId")


class DescribeLiveCertsRequest(AbstractModel):
    """DescribeLiveCerts request structure.

    """


class DescribeLiveCertsResponse(AbstractModel):
    """DescribeLiveCerts response structure.

    """

    def __init__(self):
        """
        :param CertInfoSet: Certificate information list.
        :type CertInfoSet: list of CertInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CertInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CertInfoSet") is not None:
            self.CertInfoSet = []
            for item in params.get("CertInfoSet"):
                obj = CertInfo()
                obj._deserialize(item)
                self.CertInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveDelayInfoListRequest(AbstractModel):
    """DescribeLiveDelayInfoList request structure.

    """


class DescribeLiveDelayInfoListResponse(AbstractModel):
    """DescribeLiveDelayInfoList response structure.

    """

    def __init__(self):
        """
        :param DelayInfoList: Delayed playback information list.
        :type DelayInfoList: list of DelayInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DelayInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DelayInfoList") is not None:
            self.DelayInfoList = []
            for item in params.get("DelayInfoList"):
                obj = DelayInfo()
                obj._deserialize(item)
                self.DelayInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveDomainCertRequest(AbstractModel):
    """DescribeLiveDomainCert request structure.

    """

    def __init__(self):
        """
        :param DomainName: Playback domain name.
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")


class DescribeLiveDomainCertResponse(AbstractModel):
    """DescribeLiveDomainCert response structure.

    """

    def __init__(self):
        """
        :param DomainCertInfo: Certificate information.
        :type DomainCertInfo: :class:`tencentcloud.live.v20180801.models.DomainCertInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DomainCertInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainCertInfo") is not None:
            self.DomainCertInfo = DomainCertInfo()
            self.DomainCertInfo._deserialize(params.get("DomainCertInfo"))
        self.RequestId = params.get("RequestId")


class DescribeLiveDomainRequest(AbstractModel):
    """DescribeLiveDomain request structure.

    """

    def __init__(self):
        """
        :param DomainName: Domain name.
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")


class DescribeLiveDomainResponse(AbstractModel):
    """DescribeLiveDomain response structure.

    """

    def __init__(self):
        """
        :param DomainInfo: Domain name information.
        :type DomainInfo: :class:`tencentcloud.live.v20180801.models.DomainInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DomainInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainInfo") is not None:
            self.DomainInfo = DomainInfo()
            self.DomainInfo._deserialize(params.get("DomainInfo"))
        self.RequestId = params.get("RequestId")


class DescribeLiveDomainsRequest(AbstractModel):
    """DescribeLiveDomains request structure.

    """

    def __init__(self):
        """
        :param DomainStatus: Filter by domain name status. 0: disabled, 1: enabled.
        :type DomainStatus: int
        :param DomainType: Filter by domain name type. 0: push. 1: playback
        :type DomainType: int
        :param PageSize: Number of entries per page. Value range: 10–100. Default value: 10.
        :type PageSize: int
        :param PageNum: Page number to get. Value range: 1–100000. Default value: 1.
        :type PageNum: int
        :param IsDelayLive: 0: LVB, 1: LCB. Default value: 0.
        :type IsDelayLive: int
        :param DomainPrefix: Domain name prefix.
        :type DomainPrefix: str
        """
        self.DomainStatus = None
        self.DomainType = None
        self.PageSize = None
        self.PageNum = None
        self.IsDelayLive = None
        self.DomainPrefix = None


    def _deserialize(self, params):
        self.DomainStatus = params.get("DomainStatus")
        self.DomainType = params.get("DomainType")
        self.PageSize = params.get("PageSize")
        self.PageNum = params.get("PageNum")
        self.IsDelayLive = params.get("IsDelayLive")
        self.DomainPrefix = params.get("DomainPrefix")


class DescribeLiveDomainsResponse(AbstractModel):
    """DescribeLiveDomains response structure.

    """

    def __init__(self):
        """
        :param AllCount: Total number of results.
        :type AllCount: int
        :param DomainList: List of domain name details.
        :type DomainList: list of DomainInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AllCount = None
        self.DomainList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AllCount = params.get("AllCount")
        if params.get("DomainList") is not None:
            self.DomainList = []
            for item in params.get("DomainList"):
                obj = DomainInfo()
                obj._deserialize(item)
                self.DomainList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveForbidStreamListRequest(AbstractModel):
    """DescribeLiveForbidStreamList request structure.

    """

    def __init__(self):
        """
        :param PageNum: Page number to get. Default value: 1.
        :type PageNum: int
        :param PageSize: Number of entries per page. Maximum value: 100. 
Value: any integer between 1 and 100.
Default value: 10.
        :type PageSize: int
        """
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")


class DescribeLiveForbidStreamListResponse(AbstractModel):
    """DescribeLiveForbidStreamList response structure.

    """

    def __init__(self):
        """
        :param TotalNum: Total number of eligible ones.
        :type TotalNum: int
        :param TotalPage: Total number of pages.
        :type TotalPage: int
        :param PageNum: Page number.
        :type PageNum: int
        :param PageSize: Number of entries displayed per page.
        :type PageSize: int
        :param ForbidStreamList: List of forbidden streams.
        :type ForbidStreamList: list of ForbidStreamInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalNum = None
        self.TotalPage = None
        self.PageNum = None
        self.PageSize = None
        self.ForbidStreamList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        if params.get("ForbidStreamList") is not None:
            self.ForbidStreamList = []
            for item in params.get("ForbidStreamList"):
                obj = ForbidStreamInfo()
                obj._deserialize(item)
                self.ForbidStreamList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLivePlayAuthKeyRequest(AbstractModel):
    """DescribeLivePlayAuthKey request structure.

    """

    def __init__(self):
        """
        :param DomainName: Domain name.
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")


class DescribeLivePlayAuthKeyResponse(AbstractModel):
    """DescribeLivePlayAuthKey response structure.

    """

    def __init__(self):
        """
        :param PlayAuthKeyInfo: Playback authentication key information.
        :type PlayAuthKeyInfo: :class:`tencentcloud.live.v20180801.models.PlayAuthKeyInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PlayAuthKeyInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlayAuthKeyInfo") is not None:
            self.PlayAuthKeyInfo = PlayAuthKeyInfo()
            self.PlayAuthKeyInfo._deserialize(params.get("PlayAuthKeyInfo"))
        self.RequestId = params.get("RequestId")


class DescribeLivePushAuthKeyRequest(AbstractModel):
    """DescribeLivePushAuthKey request structure.

    """

    def __init__(self):
        """
        :param DomainName: Push domain name.
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")


class DescribeLivePushAuthKeyResponse(AbstractModel):
    """DescribeLivePushAuthKey response structure.

    """

    def __init__(self):
        """
        :param PushAuthKeyInfo: Push authentication key information.
        :type PushAuthKeyInfo: :class:`tencentcloud.live.v20180801.models.PushAuthKeyInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PushAuthKeyInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PushAuthKeyInfo") is not None:
            self.PushAuthKeyInfo = PushAuthKeyInfo()
            self.PushAuthKeyInfo._deserialize(params.get("PushAuthKeyInfo"))
        self.RequestId = params.get("RequestId")


class DescribeLiveRecordRulesRequest(AbstractModel):
    """DescribeLiveRecordRules request structure.

    """


class DescribeLiveRecordRulesResponse(AbstractModel):
    """DescribeLiveRecordRules response structure.

    """

    def __init__(self):
        """
        :param Rules: List of rules.
        :type Rules: list of RuleInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveRecordTemplateRequest(AbstractModel):
    """DescribeLiveRecordTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class DescribeLiveRecordTemplateResponse(AbstractModel):
    """DescribeLiveRecordTemplate response structure.

    """

    def __init__(self):
        """
        :param Template: Recording template information.
        :type Template: :class:`tencentcloud.live.v20180801.models.RecordTemplateInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = RecordTemplateInfo()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")


class DescribeLiveRecordTemplatesRequest(AbstractModel):
    """DescribeLiveRecordTemplates request structure.

    """

    def __init__(self):
        """
        :param IsDelayLive: Whether it is an LCB template. Default value: 0.
0: LVB.
1: LCB.
        :type IsDelayLive: int
        """
        self.IsDelayLive = None


    def _deserialize(self, params):
        self.IsDelayLive = params.get("IsDelayLive")


class DescribeLiveRecordTemplatesResponse(AbstractModel):
    """DescribeLiveRecordTemplates response structure.

    """

    def __init__(self):
        """
        :param Templates: Recording template information list.
        :type Templates: list of RecordTemplateInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Templates = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = RecordTemplateInfo()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveSnapshotRulesRequest(AbstractModel):
    """DescribeLiveSnapshotRules request structure.

    """


class DescribeLiveSnapshotRulesResponse(AbstractModel):
    """DescribeLiveSnapshotRules response structure.

    """

    def __init__(self):
        """
        :param Rules: Rule list.
        :type Rules: list of RuleInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveSnapshotTemplateRequest(AbstractModel):
    """DescribeLiveSnapshotTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
Template ID returned by the [CreateLiveSnapshotTemplate](/document/product/267/32624) API call.
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class DescribeLiveSnapshotTemplateResponse(AbstractModel):
    """DescribeLiveSnapshotTemplate response structure.

    """

    def __init__(self):
        """
        :param Template: Screencapturing template information.
        :type Template: :class:`tencentcloud.live.v20180801.models.SnapshotTemplateInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = SnapshotTemplateInfo()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")


class DescribeLiveSnapshotTemplatesRequest(AbstractModel):
    """DescribeLiveSnapshotTemplates request structure.

    """


class DescribeLiveSnapshotTemplatesResponse(AbstractModel):
    """DescribeLiveSnapshotTemplates response structure.

    """

    def __init__(self):
        """
        :param Templates: Screencapturing template list.
        :type Templates: list of SnapshotTemplateInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Templates = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = SnapshotTemplateInfo()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveStreamEventListRequest(AbstractModel):
    """DescribeLiveStreamEventList request structure.

    """

    def __init__(self):
        """
        :param StartTime: Start time. 
In UTC format, such as 2018-12-29T19:00:00Z.
This supports querying the history of 60 days.
        :type StartTime: str
        :param EndTime: End time.
In UTC format, such as 2018-12-29T20:00:00Z.
This cannot be after the current time and cannot be more than 30 days after the start time.
        :type EndTime: str
        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.
        :type AppName: str
        :param DomainName: Push domain name.
        :type DomainName: str
        :param StreamName: Stream name; query with wildcard (*) is not supported; fuzzy match by default.
The IsStrict field can be used to change to exact query.
        :type StreamName: str
        :param PageNum: Page number to get.
Default value: 1.
Note: Currently, query for up to 10,000 entries is supported.
        :type PageNum: int
        :param PageSize: Number of entries per page.
Maximum value: 100.
Value range: any integer between 1 and 100.
Default value: 10.
Note: Currently, query for up to 10,000 entries is supported.
        :type PageSize: int
        :param IsFilter: Whether to filter. No filtering by default.
0: No filtering at all.
1: Filter out the failing streams and return only the successful ones.
        :type IsFilter: int
        :param IsStrict: Whether to query exactly. Fuzzy match by default.
0: Fuzzy match.
1: Exact query.
Note: This parameter takes effect when StreamName is used.
        :type IsStrict: int
        :param IsAsc: Whether to display in ascending order by end time. Descending order by default.
0: Descending.
1: Ascending.
        :type IsAsc: int
        """
        self.StartTime = None
        self.EndTime = None
        self.AppName = None
        self.DomainName = None
        self.StreamName = None
        self.PageNum = None
        self.PageSize = None
        self.IsFilter = None
        self.IsStrict = None
        self.IsAsc = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.IsFilter = params.get("IsFilter")
        self.IsStrict = params.get("IsStrict")
        self.IsAsc = params.get("IsAsc")


class DescribeLiveStreamEventListResponse(AbstractModel):
    """DescribeLiveStreamEventList response structure.

    """

    def __init__(self):
        """
        :param EventList: List of streaming events.
        :type EventList: list of StreamEventInfo
        :param PageNum: Page number.
        :type PageNum: int
        :param PageSize: Number of entries per page.
        :type PageSize: int
        :param TotalNum: Total number of eligible ones.
        :type TotalNum: int
        :param TotalPage: Total number of pages.
        :type TotalPage: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EventList = None
        self.PageNum = None
        self.PageSize = None
        self.TotalNum = None
        self.TotalPage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EventList") is not None:
            self.EventList = []
            for item in params.get("EventList"):
                obj = StreamEventInfo()
                obj._deserialize(item)
                self.EventList.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.RequestId = params.get("RequestId")


class DescribeLiveStreamOnlineListRequest(AbstractModel):
    """DescribeLiveStreamOnlineList request structure.

    """

    def __init__(self):
        """
        :param DomainName: Push domain name. If you use multiple paths, enter the `DomainName`.
        :type DomainName: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default. If you use multiple paths, enter the `AppName`.
        :type AppName: str
        :param PageNum: Page number to get. Default value: 1.
        :type PageNum: int
        :param PageSize: Number of entries per page. Maximum value: 100. 
Value: any integer between 10 and 100.
Default value: 10.
        :type PageSize: int
        :param StreamName: Stream name, which is used for exact query.
        :type StreamName: str
        """
        self.DomainName = None
        self.AppName = None
        self.PageNum = None
        self.PageSize = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.StreamName = params.get("StreamName")


class DescribeLiveStreamOnlineListResponse(AbstractModel):
    """DescribeLiveStreamOnlineList response structure.

    """

    def __init__(self):
        """
        :param TotalNum: Total number of eligible ones.
        :type TotalNum: int
        :param TotalPage: Total number of pages.
        :type TotalPage: int
        :param PageNum: Page number.
        :type PageNum: int
        :param PageSize: Number of entries displayed per page.
        :type PageSize: int
        :param OnlineInfo: Active push information list.
        :type OnlineInfo: list of StreamOnlineInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalNum = None
        self.TotalPage = None
        self.PageNum = None
        self.PageSize = None
        self.OnlineInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        if params.get("OnlineInfo") is not None:
            self.OnlineInfo = []
            for item in params.get("OnlineInfo"):
                obj = StreamOnlineInfo()
                obj._deserialize(item)
                self.OnlineInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveStreamPublishedListRequest(AbstractModel):
    """DescribeLiveStreamPublishedList request structure.

    """

    def __init__(self):
        """
        :param DomainName: Your push domain name.
        :type DomainName: str
        :param EndTime: End time.
In UTC format, such as 2016-06-30T19:00:00Z.
This cannot be after the current time.
Note: The difference between EndTime and StartTime cannot be greater than 30 days.
        :type EndTime: str
        :param StartTime: Start time. 
In UTC format, such as 2016-06-29T19:00:00Z.
This supports querying data in the past 60 days.
        :type StartTime: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default. Fuzzy match is not supported.
        :type AppName: str
        :param PageNum: Page number to get.
Default value: 1.
        :type PageNum: int
        :param PageSize: Number of entries per page.
Maximum value: 100.
Value range: any integer between 1 and 100.
Default value: 10.
        :type PageSize: int
        :param StreamName: Stream name, which supports fuzzy match.
        :type StreamName: str
        """
        self.DomainName = None
        self.EndTime = None
        self.StartTime = None
        self.AppName = None
        self.PageNum = None
        self.PageSize = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.AppName = params.get("AppName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.StreamName = params.get("StreamName")


class DescribeLiveStreamPublishedListResponse(AbstractModel):
    """DescribeLiveStreamPublishedList response structure.

    """

    def __init__(self):
        """
        :param PublishInfo: Push record information.
        :type PublishInfo: list of StreamName
        :param PageNum: Page number.
        :type PageNum: int
        :param PageSize: Number of entries per page
        :type PageSize: int
        :param TotalNum: Total number of eligible ones.
        :type TotalNum: int
        :param TotalPage: Total number of pages.
        :type TotalPage: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PublishInfo = None
        self.PageNum = None
        self.PageSize = None
        self.TotalNum = None
        self.TotalPage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PublishInfo") is not None:
            self.PublishInfo = []
            for item in params.get("PublishInfo"):
                obj = StreamName()
                obj._deserialize(item)
                self.PublishInfo.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.RequestId = params.get("RequestId")


class DescribeLiveStreamStateRequest(AbstractModel):
    """DescribeLiveStreamState request structure.

    """

    def __init__(self):
        """
        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.
        :type AppName: str
        :param DomainName: Your push domain name.
        :type DomainName: str
        :param StreamName: Stream name.
        :type StreamName: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")


class DescribeLiveStreamStateResponse(AbstractModel):
    """DescribeLiveStreamState response structure.

    """

    def __init__(self):
        """
        :param StreamState: Stream status,
active: active
inactive: Inactive
forbid: forbidden.
        :type StreamState: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.StreamState = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StreamState = params.get("StreamState")
        self.RequestId = params.get("RequestId")


class DescribeLiveTranscodeRulesRequest(AbstractModel):
    """DescribeLiveTranscodeRules request structure.

    """


class DescribeLiveTranscodeRulesResponse(AbstractModel):
    """DescribeLiveTranscodeRules response structure.

    """

    def __init__(self):
        """
        :param Rules: List of transcoding rules.
        :type Rules: list of RuleInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveTranscodeTemplateRequest(AbstractModel):
    """DescribeLiveTranscodeTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
Note: get the template ID in the returned value of the [CreateLiveTranscodeTemplate](/document/product/267/32646) API call.
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")


class DescribeLiveTranscodeTemplateResponse(AbstractModel):
    """DescribeLiveTranscodeTemplate response structure.

    """

    def __init__(self):
        """
        :param Template: Template information.
        :type Template: :class:`tencentcloud.live.v20180801.models.TemplateInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = TemplateInfo()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")


class DescribeLiveTranscodeTemplatesRequest(AbstractModel):
    """DescribeLiveTranscodeTemplates request structure.

    """


class DescribeLiveTranscodeTemplatesResponse(AbstractModel):
    """DescribeLiveTranscodeTemplates response structure.

    """

    def __init__(self):
        """
        :param Templates: List of transcoding templates.
        :type Templates: list of TemplateInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Templates = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = TemplateInfo()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveWatermarkRequest(AbstractModel):
    """DescribeLiveWatermark request structure.

    """

    def __init__(self):
        """
        :param WatermarkId: Watermark ID.
        :type WatermarkId: int
        """
        self.WatermarkId = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")


class DescribeLiveWatermarkResponse(AbstractModel):
    """DescribeLiveWatermark response structure.

    """

    def __init__(self):
        """
        :param Watermark: Watermark information.
        :type Watermark: :class:`tencentcloud.live.v20180801.models.WatermarkInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Watermark = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Watermark") is not None:
            self.Watermark = WatermarkInfo()
            self.Watermark._deserialize(params.get("Watermark"))
        self.RequestId = params.get("RequestId")


class DescribeLiveWatermarkRulesRequest(AbstractModel):
    """DescribeLiveWatermarkRules request structure.

    """


class DescribeLiveWatermarkRulesResponse(AbstractModel):
    """DescribeLiveWatermarkRules response structure.

    """

    def __init__(self):
        """
        :param Rules: Watermarking rule list.
        :type Rules: list of RuleInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveWatermarksRequest(AbstractModel):
    """DescribeLiveWatermarks request structure.

    """


class DescribeLiveWatermarksResponse(AbstractModel):
    """DescribeLiveWatermarks response structure.

    """

    def __init__(self):
        """
        :param TotalNum: Total number of watermarks.
        :type TotalNum: int
        :param WatermarkList: Watermark information list.
        :type WatermarkList: list of WatermarkInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalNum = None
        self.WatermarkList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("WatermarkList") is not None:
            self.WatermarkList = []
            for item in params.get("WatermarkList"):
                obj = WatermarkInfo()
                obj._deserialize(item)
                self.WatermarkList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProIspPlaySumInfoListRequest(AbstractModel):
    """DescribeProIspPlaySumInfoList request structure.

    """

    def __init__(self):
        """
        :param StartTime: Start time (Beijing time).
In the format of `yyyy-mm-dd HH:MM:SS`.
        :type StartTime: str
        :param EndTime: End time (Beijing time).
In the format of `yyyy-mm-dd HH:MM:SS`.
Note: `EndTime` and `StartTime` only support querying data for the last day.
        :type EndTime: str
        :param StatType: Statistics type. Valid values: Province, Isp, CountryOrArea.
        :type StatType: str
        :param PlayDomains: If this parameter is left empty, full data will be queried.
        :type PlayDomains: list of str
        :param PageNum: Page number. Value range: [1,1000]. Default value: 1.
        :type PageNum: int
        :param PageSize: Number of entries per page. Value range: [1,1000]. Default value: 20.
        :type PageSize: int
        :param MainlandOrOversea: Region. Valid values: Mainland (data for Mainland China), Oversea (data for regions outside Mainland China), China (data for China, including Hong Kong, Macao, and Taiwan), Foreign (data for regions outside China, excluding Hong Kong, Macao, and Taiwan), Global (default). If this parameter is left empty, data for all regions will be queried.
        :type MainlandOrOversea: str
        :param OutLanguage: Language used in the output field. Valid values: Chinese (default), English. Currently, country/region, district, and ISP parameters support multiple languages.
        :type OutLanguage: str
        """
        self.StartTime = None
        self.EndTime = None
        self.StatType = None
        self.PlayDomains = None
        self.PageNum = None
        self.PageSize = None
        self.MainlandOrOversea = None
        self.OutLanguage = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.StatType = params.get("StatType")
        self.PlayDomains = params.get("PlayDomains")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.OutLanguage = params.get("OutLanguage")


class DescribeProIspPlaySumInfoListResponse(AbstractModel):
    """DescribeProIspPlaySumInfoList response structure.

    """

    def __init__(self):
        """
        :param TotalFlux: Total traffic.
        :type TotalFlux: float
        :param TotalRequest: Total number of requests.
        :type TotalRequest: int
        :param StatType: Statistics type.
        :type StatType: str
        :param PageSize: Number of results per page.
        :type PageSize: int
        :param PageNum: Page number.
        :type PageNum: int
        :param TotalNum: Total number of results.
        :type TotalNum: int
        :param TotalPage: Total number of pages.
        :type TotalPage: int
        :param DataInfoList: Aggregated data list by district, ISP, or country/region.
        :type DataInfoList: list of ProIspPlaySumInfo
        :param AvgFluxPerSecond: Average bandwidth.
        :type AvgFluxPerSecond: float
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalFlux = None
        self.TotalRequest = None
        self.StatType = None
        self.PageSize = None
        self.PageNum = None
        self.TotalNum = None
        self.TotalPage = None
        self.DataInfoList = None
        self.AvgFluxPerSecond = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalFlux = params.get("TotalFlux")
        self.TotalRequest = params.get("TotalRequest")
        self.StatType = params.get("StatType")
        self.PageSize = params.get("PageSize")
        self.PageNum = params.get("PageNum")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = ProIspPlaySumInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.AvgFluxPerSecond = params.get("AvgFluxPerSecond")
        self.RequestId = params.get("RequestId")


class DescribeStreamDayPlayInfoListRequest(AbstractModel):
    """DescribeStreamDayPlayInfoList request structure.

    """

    def __init__(self):
        """
        :param DayTime: Date in the format of `YYYY-mm-dd`.
Data is available at 3 AM the next day. You are recommended to query the latest data after this time point.
        :type DayTime: str
        :param PlayDomain: Playback domain name.
        :type PlayDomain: str
        :param PageNum: Page number. Value range: [1,1000]. Default value: 1.
        :type PageNum: int
        :param PageSize: Number of entries per page. Value range: [100,1000]. Default value: 1,000.
        :type PageSize: int
        """
        self.DayTime = None
        self.PlayDomain = None
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.DayTime = params.get("DayTime")
        self.PlayDomain = params.get("PlayDomain")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")


class DescribeStreamDayPlayInfoListResponse(AbstractModel):
    """DescribeStreamDayPlayInfoList response structure.

    """

    def __init__(self):
        """
        :param DataInfoList: Playback data information list.
        :type DataInfoList: list of PlayDataInfoByStream
        :param TotalNum: Total number.
        :type TotalNum: int
        :param TotalPage: Total number of pages.
        :type TotalPage: int
        :param PageNum: Page number where the current data resides.
        :type PageNum: int
        :param PageSize: Number of entries per page.
        :type PageSize: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DataInfoList = None
        self.TotalNum = None
        self.TotalPage = None
        self.PageNum = None
        self.PageSize = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PlayDataInfoByStream()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.RequestId = params.get("RequestId")


class DescribeStreamPushInfoListRequest(AbstractModel):
    """DescribeStreamPushInfoList request structure.

    """

    def __init__(self):
        """
        :param StreamName: Stream name.
        :type StreamName: str
        :param StartTime: Start time point in the format of `yyyy-mm-dd HH:MM:SS`.
        :type StartTime: str
        :param EndTime: End time point in the format of `yyyy-mm-dd HH:MM:SS`. The maximum time span is 6 hours. Data for the last 6 days can be queried.
        :type EndTime: str
        :param PushDomain: Push domain name.
        :type PushDomain: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        """
        self.StreamName = None
        self.StartTime = None
        self.EndTime = None
        self.PushDomain = None
        self.AppName = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PushDomain = params.get("PushDomain")
        self.AppName = params.get("AppName")


class DescribeStreamPushInfoListResponse(AbstractModel):
    """DescribeStreamPushInfoList response structure.

    """

    def __init__(self):
        """
        :param DataInfoList: Returned data list.
        :type DataInfoList: list of PushQualityData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PushQualityData()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DomainCertInfo(AbstractModel):
    """Domain name certificate information

    """

    def __init__(self):
        """
        :param CertId: Certificate ID.
        :type CertId: int
        :param CertName: Certificate name.
        :type CertName: str
        :param Description: Description.
        :type Description: str
        :param CreateTime: Creation time in UTC format.
        :type CreateTime: str
        :param HttpsCrt: Certificate content.
        :type HttpsCrt: str
        :param CertType: Certificate type.
0: user-added certificate
1: Tencent Cloud-hosted certificate.
        :type CertType: int
        :param CertExpireTime: Certificate expiration time in UTC format.
        :type CertExpireTime: str
        :param DomainName: Domain name that uses this certificate.
        :type DomainName: str
        :param Status: Certificate status.
        :type Status: int
        """
        self.CertId = None
        self.CertName = None
        self.Description = None
        self.CreateTime = None
        self.HttpsCrt = None
        self.CertType = None
        self.CertExpireTime = None
        self.DomainName = None
        self.Status = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.CertName = params.get("CertName")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.HttpsCrt = params.get("HttpsCrt")
        self.CertType = params.get("CertType")
        self.CertExpireTime = params.get("CertExpireTime")
        self.DomainName = params.get("DomainName")
        self.Status = params.get("Status")


class DomainInfo(AbstractModel):
    """LVB domain name information

    """

    def __init__(self):
        """
        :param Name: LVB domain name.
        :type Name: str
        :param Type: Domain name type:
0: push.
1: playback.
        :type Type: int
        :param Status: Domain name status:
0: deactivated.
1: activated.
        :type Status: int
        :param CreateTime: Creation time.
        :type CreateTime: str
        :param BCName: Whether there is a CNAME record pointing to a fixed rule domain name:
0: no.
1: yes.
        :type BCName: int
        :param TargetDomain: Domain name corresponding to CNAME record.
        :type TargetDomain: str
        :param PlayType: Playback region. This parameter is valid only if `Type` is 1.
1: in Mainland China.
2: global.
3: outside Mainland China.
        :type PlayType: int
        :param IsDelayLive: Whether it is LCB:
0: LVB.
1: LCB.
        :type IsDelayLive: int
        :param CurrentCName: Information of currently used CNAME record.
        :type CurrentCName: str
        :param RentTag: Disused parameter, which can be ignored.
        :type RentTag: int
        :param RentExpireTime: Disused parameter, which can be ignored.
        :type RentExpireTime: str
        :param IsMiniProgramLive: 0: LVB.
1: LVB on Mini Program.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsMiniProgramLive: int
        """
        self.Name = None
        self.Type = None
        self.Status = None
        self.CreateTime = None
        self.BCName = None
        self.TargetDomain = None
        self.PlayType = None
        self.IsDelayLive = None
        self.CurrentCName = None
        self.RentTag = None
        self.RentExpireTime = None
        self.IsMiniProgramLive = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.BCName = params.get("BCName")
        self.TargetDomain = params.get("TargetDomain")
        self.PlayType = params.get("PlayType")
        self.IsDelayLive = params.get("IsDelayLive")
        self.CurrentCName = params.get("CurrentCName")
        self.RentTag = params.get("RentTag")
        self.RentExpireTime = params.get("RentExpireTime")
        self.IsMiniProgramLive = params.get("IsMiniProgramLive")


class DropLiveStreamRequest(AbstractModel):
    """DropLiveStream request structure.

    """

    def __init__(self):
        """
        :param StreamName: Stream name.
        :type StreamName: str
        :param DomainName: Your acceleration domain name.
        :type DomainName: str
        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.
        :type AppName: str
        """
        self.StreamName = None
        self.DomainName = None
        self.AppName = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")


class DropLiveStreamResponse(AbstractModel):
    """DropLiveStream response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableLiveDomainRequest(AbstractModel):
    """EnableLiveDomain request structure.

    """

    def __init__(self):
        """
        :param DomainName: LVB domain name to be enabled.
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")


class EnableLiveDomainResponse(AbstractModel):
    """EnableLiveDomain response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ForbidLiveDomainRequest(AbstractModel):
    """ForbidLiveDomain request structure.

    """

    def __init__(self):
        """
        :param DomainName: LVB domain name to be disabled.
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")


class ForbidLiveDomainResponse(AbstractModel):
    """ForbidLiveDomain response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ForbidLiveStreamRequest(AbstractModel):
    """ForbidLiveStream request structure.

    """

    def __init__(self):
        """
        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.
        :type AppName: str
        :param DomainName: Your push domain name.
        :type DomainName: str
        :param StreamName: Stream name.
        :type StreamName: str
        :param ResumeTime: Time to resume the stream in UTC format, such as 2018-11-29T19:00:00Z.
Notes:
1. The duration of forbidding is 7 days by default and can be up to 90 days.
2. The Beijing time is in UTC+8. This value should be in the format as required by ISO 8601. For more information, please see [ISO Date and Time Format](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type ResumeTime: str
        :param Reason: Reason for forbidding.
Note: Be sure to enter the reason for forbidding to avoid any faulty operations.
Length limit: 2,048 bytes.
        :type Reason: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None
        self.ResumeTime = None
        self.Reason = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        self.ResumeTime = params.get("ResumeTime")
        self.Reason = params.get("Reason")


class ForbidLiveStreamResponse(AbstractModel):
    """ForbidLiveStream response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ForbidStreamInfo(AbstractModel):
    """List of forbidden streams

    """

    def __init__(self):
        """
        :param StreamName: Stream name.
        :type StreamName: str
        :param CreateTime: Creation time.
        :type CreateTime: str
        :param ExpireTime: Forbidding expiration time.
        :type ExpireTime: str
        """
        self.StreamName = None
        self.CreateTime = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")


class GroupProIspDataInfo(AbstractModel):
    """Bandwidth, traffic, number of requests, and number of concurrent connections of an ISP in a district.

    """

    def __init__(self):
        """
        :param ProvinceName: District.
        :type ProvinceName: str
        :param IspName: ISP.
        :type IspName: str
        :param DetailInfoList: Detailed data at the minute level.
        :type DetailInfoList: list of CdnPlayStatData
        """
        self.ProvinceName = None
        self.IspName = None
        self.DetailInfoList = None


    def _deserialize(self, params):
        self.ProvinceName = params.get("ProvinceName")
        self.IspName = params.get("IspName")
        if params.get("DetailInfoList") is not None:
            self.DetailInfoList = []
            for item in params.get("DetailInfoList"):
                obj = CdnPlayStatData()
                obj._deserialize(item)
                self.DetailInfoList.append(obj)


class HlsSpecialParam(AbstractModel):
    """HLS-specific recording parameter

    """

    def __init__(self):
        """
        :param FlowContinueDuration: HLS timeout period.
        :type FlowContinueDuration: int
        """
        self.FlowContinueDuration = None


    def _deserialize(self, params):
        self.FlowContinueDuration = params.get("FlowContinueDuration")


class ModifyLiveCallbackTemplateRequest(AbstractModel):
    """ModifyLiveCallbackTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param TemplateName: Template name.
        :type TemplateName: str
        :param Description: Description.
        :type Description: str
        :param StreamBeginNotifyUrl: Stream starting callback URL.
        :type StreamBeginNotifyUrl: str
        :param StreamEndNotifyUrl: Interruption callback URL.
        :type StreamEndNotifyUrl: str
        :param RecordNotifyUrl: Recording callback URL.
        :type RecordNotifyUrl: str
        :param SnapshotNotifyUrl: Screencapturing callback URL.
        :type SnapshotNotifyUrl: str
        :param PornCensorshipNotifyUrl: Porn detection callback URL.
        :type PornCensorshipNotifyUrl: str
        :param CallbackKey: Callback key. The callback URL is public. For the callback signature, please see the event message notification document.
[Event Message Notification](/document/product/267/32744).
        :type CallbackKey: str
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.StreamBeginNotifyUrl = None
        self.StreamEndNotifyUrl = None
        self.RecordNotifyUrl = None
        self.SnapshotNotifyUrl = None
        self.PornCensorshipNotifyUrl = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.StreamBeginNotifyUrl = params.get("StreamBeginNotifyUrl")
        self.StreamEndNotifyUrl = params.get("StreamEndNotifyUrl")
        self.RecordNotifyUrl = params.get("RecordNotifyUrl")
        self.SnapshotNotifyUrl = params.get("SnapshotNotifyUrl")
        self.PornCensorshipNotifyUrl = params.get("PornCensorshipNotifyUrl")
        self.CallbackKey = params.get("CallbackKey")


class ModifyLiveCallbackTemplateResponse(AbstractModel):
    """ModifyLiveCallbackTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveCertRequest(AbstractModel):
    """ModifyLiveCert request structure.

    """

    def __init__(self):
        """
        :param CertId: Certificate ID.
        :type CertId: str
        :param CertType: Certificate type. 0: user-added certificate, 1: Tencent Cloud-hosted certificate.
        :type CertType: int
        :param CertName: Certificate name.
        :type CertName: str
        :param HttpsCrt: Certificate content, i.e., public key.
        :type HttpsCrt: str
        :param HttpsKey: Private key.
        :type HttpsKey: str
        :param Description: Description.
        :type Description: str
        """
        self.CertId = None
        self.CertType = None
        self.CertName = None
        self.HttpsCrt = None
        self.HttpsKey = None
        self.Description = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.CertType = params.get("CertType")
        self.CertName = params.get("CertName")
        self.HttpsCrt = params.get("HttpsCrt")
        self.HttpsKey = params.get("HttpsKey")
        self.Description = params.get("Description")


class ModifyLiveCertResponse(AbstractModel):
    """ModifyLiveCert response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveDomainCertRequest(AbstractModel):
    """ModifyLiveDomainCert request structure.

    """

    def __init__(self):
        """
        :param DomainName: Playback domain name.
        :type DomainName: str
        :param CertId: Certificate ID.
        :type CertId: int
        :param Status: Status. 0: off, 1: on.
        :type Status: int
        """
        self.DomainName = None
        self.CertId = None
        self.Status = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.CertId = params.get("CertId")
        self.Status = params.get("Status")


class ModifyLiveDomainCertResponse(AbstractModel):
    """ModifyLiveDomainCert response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLivePlayAuthKeyRequest(AbstractModel):
    """ModifyLivePlayAuthKey request structure.

    """

    def __init__(self):
        """
        :param DomainName: Domain name.
        :type DomainName: str
        :param Enable: Whether to enable. 0: disabled; 1: enabled.
        :type Enable: int
        :param AuthKey: Authentication key.
        :type AuthKey: str
        :param AuthDelta: Validity period in seconds.
        :type AuthDelta: int
        :param AuthBackKey: Authentication backkey.
        :type AuthBackKey: str
        """
        self.DomainName = None
        self.Enable = None
        self.AuthKey = None
        self.AuthDelta = None
        self.AuthBackKey = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.AuthKey = params.get("AuthKey")
        self.AuthDelta = params.get("AuthDelta")
        self.AuthBackKey = params.get("AuthBackKey")


class ModifyLivePlayAuthKeyResponse(AbstractModel):
    """ModifyLivePlayAuthKey response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLivePlayDomainRequest(AbstractModel):
    """ModifyLivePlayDomain request structure.

    """

    def __init__(self):
        """
        :param DomainName: Playback domain name.
        :type DomainName: str
        :param PlayType: Pull domain name type. 1: Mainland China. 2: global, 3: outside Mainland China
        :type PlayType: int
        """
        self.DomainName = None
        self.PlayType = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.PlayType = params.get("PlayType")


class ModifyLivePlayDomainResponse(AbstractModel):
    """ModifyLivePlayDomain response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLivePushAuthKeyRequest(AbstractModel):
    """ModifyLivePushAuthKey request structure.

    """

    def __init__(self):
        """
        :param DomainName: Push domain name.
        :type DomainName: str
        :param Enable: Whether to enable. 0: disabled; 1: enabled.
        :type Enable: int
        :param MasterAuthKey: Master authentication key.
        :type MasterAuthKey: str
        :param BackupAuthKey: Backup authentication key.
        :type BackupAuthKey: str
        :param AuthDelta: Validity period in seconds.
        :type AuthDelta: int
        """
        self.DomainName = None
        self.Enable = None
        self.MasterAuthKey = None
        self.BackupAuthKey = None
        self.AuthDelta = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.MasterAuthKey = params.get("MasterAuthKey")
        self.BackupAuthKey = params.get("BackupAuthKey")
        self.AuthDelta = params.get("AuthDelta")


class ModifyLivePushAuthKeyResponse(AbstractModel):
    """ModifyLivePushAuthKey response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveRecordTemplateRequest(AbstractModel):
    """ModifyLiveRecordTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param TemplateName: Template name.
        :type TemplateName: str
        :param Description: Message description
        :type Description: str
        :param FlvParam: FLV recording parameter, which is set when FLV recording is enabled.
        :type FlvParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param HlsParam: HLS recording parameter, which is set when HLS recording is enabled.
        :type HlsParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param Mp4Param: MP4 recording parameter, which is set when MP4 recording is enabled.
        :type Mp4Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param AacParam: AAC recording parameter, which is set when AAC recording is enabled.
        :type AacParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param HlsSpecialParam: Custom HLS recording parameter.
        :type HlsSpecialParam: :class:`tencentcloud.live.v20180801.models.HlsSpecialParam`
        :param Mp3Param: MP3 recording parameter, which is set when MP3 recording is enabled.
        :type Mp3Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.FlvParam = None
        self.HlsParam = None
        self.Mp4Param = None
        self.AacParam = None
        self.HlsSpecialParam = None
        self.Mp3Param = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        if params.get("FlvParam") is not None:
            self.FlvParam = RecordParam()
            self.FlvParam._deserialize(params.get("FlvParam"))
        if params.get("HlsParam") is not None:
            self.HlsParam = RecordParam()
            self.HlsParam._deserialize(params.get("HlsParam"))
        if params.get("Mp4Param") is not None:
            self.Mp4Param = RecordParam()
            self.Mp4Param._deserialize(params.get("Mp4Param"))
        if params.get("AacParam") is not None:
            self.AacParam = RecordParam()
            self.AacParam._deserialize(params.get("AacParam"))
        if params.get("HlsSpecialParam") is not None:
            self.HlsSpecialParam = HlsSpecialParam()
            self.HlsSpecialParam._deserialize(params.get("HlsSpecialParam"))
        if params.get("Mp3Param") is not None:
            self.Mp3Param = RecordParam()
            self.Mp3Param._deserialize(params.get("Mp3Param"))


class ModifyLiveRecordTemplateResponse(AbstractModel):
    """ModifyLiveRecordTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveSnapshotTemplateRequest(AbstractModel):
    """ModifyLiveSnapshotTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param TemplateName: Template name.
Maximum length: 255 bytes.
        :type TemplateName: str
        :param Description: Description.
Maximum length: 1,024 bytes.
        :type Description: str
        :param SnapshotInterval: Screencapturing interval in seconds. Default value: 10s.
Value range: 5–600s.
        :type SnapshotInterval: int
        :param Width: Screenshot width. Default value: 0 (original width).
        :type Width: int
        :param Height: Screenshot height. Default value: 0 (original height).
        :type Height: int
        :param PornFlag: Whether to enable porn detection. Default value: 0.
0: do not enable.
1: enable.
        :type PornFlag: int
        :param CosAppId: COS application ID.
        :type CosAppId: int
        :param CosBucket: COS bucket name.
        :type CosBucket: str
        :param CosRegion: COS region.
        :type CosRegion: str
        :param CosPrefix: COS bucket folder prefix.
        :type CosPrefix: str
        :param CosFileName: COS filename.
        :type CosFileName: str
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.SnapshotInterval = None
        self.Width = None
        self.Height = None
        self.PornFlag = None
        self.CosAppId = None
        self.CosBucket = None
        self.CosRegion = None
        self.CosPrefix = None
        self.CosFileName = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.SnapshotInterval = params.get("SnapshotInterval")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.PornFlag = params.get("PornFlag")
        self.CosAppId = params.get("CosAppId")
        self.CosBucket = params.get("CosBucket")
        self.CosRegion = params.get("CosRegion")
        self.CosPrefix = params.get("CosPrefix")
        self.CosFileName = params.get("CosFileName")


class ModifyLiveSnapshotTemplateResponse(AbstractModel):
    """ModifyLiveSnapshotTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveTranscodeTemplateRequest(AbstractModel):
    """ModifyLiveTranscodeTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param Vcodec: Video encoding format:
h264/h265.
        :type Vcodec: str
        :param Acodec: Audio encoding format:
aac/mp3.
        :type Acodec: str
        :param AudioBitrate: Audio bitrate. Default value: 0.
Value range: 0–500.
        :type AudioBitrate: int
        :param Description: Template description.
        :type Description: str
        :param VideoBitrate: Video bitrate. Value range: 100–8000 Kbps.
Note: the bitrate value must be a multiple of 100.
        :type VideoBitrate: int
        :param Width: Width. Value range: 0-3000.
        :type Width: int
        :param NeedVideo: Whether to keep the video. 0: no; 1: yes. Default value: 1.
        :type NeedVideo: int
        :param NeedAudio: Whether to keep the audio. 0: no; 1: yes. Default value: 1.
        :type NeedAudio: int
        :param Height: Height. Value range: 0-3000.
        :type Height: int
        :param Fps: Frame rate. Value range: 0–200.
        :type Fps: int
        :param Gop: Keyframe interval in seconds. Value range: 0–50.
        :type Gop: int
        :param Rotate: Rotation angle.
0, 90, 180, 270.
        :type Rotate: int
        :param Profile: Encoding quality:
baseline/main/high.
        :type Profile: str
        :param BitrateToOrig: Whether to not exceed the original bitrate. 0: no; 1: yes. Default value: 0.
        :type BitrateToOrig: int
        :param HeightToOrig: Whether to not exceed the original height. 0: no; 1: yes. Default value: 0.
        :type HeightToOrig: int
        :param FpsToOrig: Whether to not exceed the original frame rate. 0: no; 1: yes. Default value: 0.
        :type FpsToOrig: int
        :param AdaptBitratePercent: `VideoBitrate` minus top speed codec bitrate. Value range: 0.1–0.5.
        :type AdaptBitratePercent: float
        """
        self.TemplateId = None
        self.Vcodec = None
        self.Acodec = None
        self.AudioBitrate = None
        self.Description = None
        self.VideoBitrate = None
        self.Width = None
        self.NeedVideo = None
        self.NeedAudio = None
        self.Height = None
        self.Fps = None
        self.Gop = None
        self.Rotate = None
        self.Profile = None
        self.BitrateToOrig = None
        self.HeightToOrig = None
        self.FpsToOrig = None
        self.AdaptBitratePercent = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Vcodec = params.get("Vcodec")
        self.Acodec = params.get("Acodec")
        self.AudioBitrate = params.get("AudioBitrate")
        self.Description = params.get("Description")
        self.VideoBitrate = params.get("VideoBitrate")
        self.Width = params.get("Width")
        self.NeedVideo = params.get("NeedVideo")
        self.NeedAudio = params.get("NeedAudio")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        self.Gop = params.get("Gop")
        self.Rotate = params.get("Rotate")
        self.Profile = params.get("Profile")
        self.BitrateToOrig = params.get("BitrateToOrig")
        self.HeightToOrig = params.get("HeightToOrig")
        self.FpsToOrig = params.get("FpsToOrig")
        self.AdaptBitratePercent = params.get("AdaptBitratePercent")


class ModifyLiveTranscodeTemplateResponse(AbstractModel):
    """ModifyLiveTranscodeTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PlayAuthKeyInfo(AbstractModel):
    """Playback authentication key information.

    """

    def __init__(self):
        """
        :param DomainName: Domain name.
        :type DomainName: str
        :param Enable: Whether to enable:
0: disable.
1: enable.
        :type Enable: int
        :param AuthKey: Authentication key.
        :type AuthKey: str
        :param AuthDelta: Validity period in seconds.
        :type AuthDelta: int
        :param AuthBackKey: Authentication `BackKey`.
        :type AuthBackKey: str
        """
        self.DomainName = None
        self.Enable = None
        self.AuthKey = None
        self.AuthDelta = None
        self.AuthBackKey = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.AuthKey = params.get("AuthKey")
        self.AuthDelta = params.get("AuthDelta")
        self.AuthBackKey = params.get("AuthBackKey")


class PlayDataInfoByStream(AbstractModel):
    """Playback information at the stream level.

    """

    def __init__(self):
        """
        :param StreamName: Stream name.
        :type StreamName: str
        :param TotalFlux: Total traffic in MB.
        :type TotalFlux: float
        """
        self.StreamName = None
        self.TotalFlux = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.TotalFlux = params.get("TotalFlux")


class ProIspPlaySumInfo(AbstractModel):
    """Queries playback information by district/ISP.

    """

    def __init__(self):
        """
        :param Name: District/ISP/country/region.
        :type Name: str
        :param TotalFlux: Total traffic in MB.
        :type TotalFlux: float
        :param TotalRequest: Total number of requests.
        :type TotalRequest: int
        :param AvgFluxPerSecond: Average download traffic in MB/s.
        :type AvgFluxPerSecond: float
        """
        self.Name = None
        self.TotalFlux = None
        self.TotalRequest = None
        self.AvgFluxPerSecond = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.TotalFlux = params.get("TotalFlux")
        self.TotalRequest = params.get("TotalRequest")
        self.AvgFluxPerSecond = params.get("AvgFluxPerSecond")


class PublishTime(AbstractModel):
    """Push time.

    """

    def __init__(self):
        """
        :param PublishTime: Push time.
In UTC format, such as 2018-06-29T19:00:00Z.
        :type PublishTime: str
        """
        self.PublishTime = None


    def _deserialize(self, params):
        self.PublishTime = params.get("PublishTime")


class PushAuthKeyInfo(AbstractModel):
    """Push authentication key information.

    """

    def __init__(self):
        """
        :param DomainName: Domain name.
        :type DomainName: str
        :param Enable: Whether to enable. 0: disabled; 1: enabled.
        :type Enable: int
        :param MasterAuthKey: Master authentication key.
        :type MasterAuthKey: str
        :param BackupAuthKey: Standby authentication key.
        :type BackupAuthKey: str
        :param AuthDelta: Validity period in seconds.
        :type AuthDelta: int
        """
        self.DomainName = None
        self.Enable = None
        self.MasterAuthKey = None
        self.BackupAuthKey = None
        self.AuthDelta = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.MasterAuthKey = params.get("MasterAuthKey")
        self.BackupAuthKey = params.get("BackupAuthKey")
        self.AuthDelta = params.get("AuthDelta")


class PushQualityData(AbstractModel):
    """Push quality data of a stream.

    """

    def __init__(self):
        """
        :param Time: Data time in the format of `%Y-%m-%d %H:%M:%S.%ms` and accurate down to the millisecond level.
        :type Time: str
        :param PushDomain: Push domain name.
        :type PushDomain: str
        :param AppName: Push path.
        :type AppName: str
        :param ClientIp: Push client IP.
        :type ClientIp: str
        :param BeginPushTime: Push start time in the format of `%Y-%m-%d %H:%M:%S.%ms` and accurate down to the millisecond level.
        :type BeginPushTime: str
        :param Resolution: Resolution information.
        :type Resolution: str
        :param VCodec: Video codec.
        :type VCodec: str
        :param ACodec: Audio codec.
        :type ACodec: str
        :param Sequence: Push serial number, which uniquely identifies a push.
        :type Sequence: str
        :param VideoFps: Video frame rate.
        :type VideoFps: int
        :param VideoRate: Video bitrate in bps.
        :type VideoRate: int
        :param AudioFps: Audio frame rate.
        :type AudioFps: int
        :param AudioRate: Audio bitrate in bps.
        :type AudioRate: int
        :param LocalTs: Local elapsed time in milliseconds. The greater the difference between audio/video elapsed time and local elapsed time, the poorer the push quality and the more serious the upstream lag.
        :type LocalTs: int
        :param VideoTs: Video elapsed time in milliseconds.
        :type VideoTs: int
        :param AudioTs: Audio elapsed time in milliseconds.
        :type AudioTs: int
        :param MetaVideoRate: Video bitrate in `metadata` in Kbps.
        :type MetaVideoRate: int
        :param MetaAudioRate: Audio bitrate in `metadata` in Kbps.
        :type MetaAudioRate: int
        :param MateFps: Frame rate in `metadata`.
        :type MateFps: int
        """
        self.Time = None
        self.PushDomain = None
        self.AppName = None
        self.ClientIp = None
        self.BeginPushTime = None
        self.Resolution = None
        self.VCodec = None
        self.ACodec = None
        self.Sequence = None
        self.VideoFps = None
        self.VideoRate = None
        self.AudioFps = None
        self.AudioRate = None
        self.LocalTs = None
        self.VideoTs = None
        self.AudioTs = None
        self.MetaVideoRate = None
        self.MetaAudioRate = None
        self.MateFps = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.PushDomain = params.get("PushDomain")
        self.AppName = params.get("AppName")
        self.ClientIp = params.get("ClientIp")
        self.BeginPushTime = params.get("BeginPushTime")
        self.Resolution = params.get("Resolution")
        self.VCodec = params.get("VCodec")
        self.ACodec = params.get("ACodec")
        self.Sequence = params.get("Sequence")
        self.VideoFps = params.get("VideoFps")
        self.VideoRate = params.get("VideoRate")
        self.AudioFps = params.get("AudioFps")
        self.AudioRate = params.get("AudioRate")
        self.LocalTs = params.get("LocalTs")
        self.VideoTs = params.get("VideoTs")
        self.AudioTs = params.get("AudioTs")
        self.MetaVideoRate = params.get("MetaVideoRate")
        self.MetaAudioRate = params.get("MetaAudioRate")
        self.MateFps = params.get("MateFps")


class RecordParam(AbstractModel):
    """Recording template parameter

    """

    def __init__(self):
        """
        :param RecordInterval: Recording interval.
In seconds. Default value: 1,800.
Value range: 300–7,200.
This parameter is not valid for HLS, and a file is generated from push start to push end when HLS is recorded.
        :type RecordInterval: int
        :param StorageTime: Recording storage duration.
In seconds. Value range: 0–93,312,000.
0 represents permanent storage.
        :type StorageTime: int
        :param Enable: Whether to enable recording in the current format. 0: no; 1: yes. Default value: 0.
        :type Enable: int
        :param VodSubAppId: VOD subapplication ID.
        :type VodSubAppId: int
        :param VodFileName: Recording filename.
        :type VodFileName: str
        """
        self.RecordInterval = None
        self.StorageTime = None
        self.Enable = None
        self.VodSubAppId = None
        self.VodFileName = None


    def _deserialize(self, params):
        self.RecordInterval = params.get("RecordInterval")
        self.StorageTime = params.get("StorageTime")
        self.Enable = params.get("Enable")
        self.VodSubAppId = params.get("VodSubAppId")
        self.VodFileName = params.get("VodFileName")


class RecordTemplateInfo(AbstractModel):
    """Recording template information

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param TemplateName: Template name.
        :type TemplateName: str
        :param Description: Message description
        :type Description: str
        :param FlvParam: FLV recording parameter.
        :type FlvParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param HlsParam: HLS recording parameter.
        :type HlsParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param Mp4Param: MP4 recording parameter.
        :type Mp4Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param AacParam: AAC recording parameter.
        :type AacParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param IsDelayLive: 0: LVB,
1: LCB.
        :type IsDelayLive: int
        :param HlsSpecialParam: Custom HLS recording parameter
        :type HlsSpecialParam: :class:`tencentcloud.live.v20180801.models.HlsSpecialParam`
        :param Mp3Param: MP3 recording parameter.
        :type Mp3Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.FlvParam = None
        self.HlsParam = None
        self.Mp4Param = None
        self.AacParam = None
        self.IsDelayLive = None
        self.HlsSpecialParam = None
        self.Mp3Param = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        if params.get("FlvParam") is not None:
            self.FlvParam = RecordParam()
            self.FlvParam._deserialize(params.get("FlvParam"))
        if params.get("HlsParam") is not None:
            self.HlsParam = RecordParam()
            self.HlsParam._deserialize(params.get("HlsParam"))
        if params.get("Mp4Param") is not None:
            self.Mp4Param = RecordParam()
            self.Mp4Param._deserialize(params.get("Mp4Param"))
        if params.get("AacParam") is not None:
            self.AacParam = RecordParam()
            self.AacParam._deserialize(params.get("AacParam"))
        self.IsDelayLive = params.get("IsDelayLive")
        if params.get("HlsSpecialParam") is not None:
            self.HlsSpecialParam = HlsSpecialParam()
            self.HlsSpecialParam._deserialize(params.get("HlsSpecialParam"))
        if params.get("Mp3Param") is not None:
            self.Mp3Param = RecordParam()
            self.Mp3Param._deserialize(params.get("Mp3Param"))


class ResumeDelayLiveStreamRequest(AbstractModel):
    """ResumeDelayLiveStream request structure.

    """

    def __init__(self):
        """
        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.
        :type AppName: str
        :param DomainName: Push domain name.
        :type DomainName: str
        :param StreamName: Stream name.
        :type StreamName: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")


class ResumeDelayLiveStreamResponse(AbstractModel):
    """ResumeDelayLiveStream response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResumeLiveStreamRequest(AbstractModel):
    """ResumeLiveStream request structure.

    """

    def __init__(self):
        """
        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.
        :type AppName: str
        :param DomainName: Your push domain name.
        :type DomainName: str
        :param StreamName: Stream name.
        :type StreamName: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")


class ResumeLiveStreamResponse(AbstractModel):
    """ResumeLiveStream response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RuleInfo(AbstractModel):
    """Rule information.

    """

    def __init__(self):
        """
        :param CreateTime: Rule creation time.
        :type CreateTime: str
        :param UpdateTime: Rule update time.
        :type UpdateTime: str
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param DomainName: Push domain name.
        :type DomainName: str
        :param AppName: Push path.
        :type AppName: str
        :param StreamName: Stream name.
        :type StreamName: str
        """
        self.CreateTime = None
        self.UpdateTime = None
        self.TemplateId = None
        self.DomainName = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.TemplateId = params.get("TemplateId")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")


class SnapshotTemplateInfo(AbstractModel):
    """Screencapturing template information.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param TemplateName: Template name.
        :type TemplateName: str
        :param SnapshotInterval: Screencapturing interval. Value range: 5–300s.
        :type SnapshotInterval: int
        :param Width: Screenshot width. Value range: 0–3000. 
0: original width and fit to the original ratio.
        :type Width: int
        :param Height: Screenshot height. Value range: 0–2000.
0: original height and fit to the original ratio.
        :type Height: int
        :param PornFlag: Whether to enable porn detection. 0: no, 1: yes.
        :type PornFlag: int
        :param CosAppId: COS application ID.
        :type CosAppId: int
        :param CosBucket: COS bucket name.
        :type CosBucket: str
        :param CosRegion: COS region.
        :type CosRegion: str
        :param Description: Template description.
        :type Description: str
        :param CosPrefix: COS bucket folder prefix.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CosPrefix: str
        :param CosFileName: COS filename.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CosFileName: str
        """
        self.TemplateId = None
        self.TemplateName = None
        self.SnapshotInterval = None
        self.Width = None
        self.Height = None
        self.PornFlag = None
        self.CosAppId = None
        self.CosBucket = None
        self.CosRegion = None
        self.Description = None
        self.CosPrefix = None
        self.CosFileName = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.SnapshotInterval = params.get("SnapshotInterval")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.PornFlag = params.get("PornFlag")
        self.CosAppId = params.get("CosAppId")
        self.CosBucket = params.get("CosBucket")
        self.CosRegion = params.get("CosRegion")
        self.Description = params.get("Description")
        self.CosPrefix = params.get("CosPrefix")
        self.CosFileName = params.get("CosFileName")


class StopLiveRecordRequest(AbstractModel):
    """StopLiveRecord request structure.

    """

    def __init__(self):
        """
        :param StreamName: Stream name.
        :type StreamName: str
        :param TaskId: Task ID, which uniquely identifies the recording task globally.
        :type TaskId: int
        """
        self.StreamName = None
        self.TaskId = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.TaskId = params.get("TaskId")


class StopLiveRecordResponse(AbstractModel):
    """StopLiveRecord response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StreamEventInfo(AbstractModel):
    """Streaming event information.

    """

    def __init__(self):
        """
        :param AppName: Application name.
        :type AppName: str
        :param DomainName: Push domain name.
        :type DomainName: str
        :param StreamName: Stream name.
        :type StreamName: str
        :param StreamStartTime: Push start time.
In UTC format, such as 2019-01-07T12:00:00Z.
        :type StreamStartTime: str
        :param StreamEndTime: Push end time.
In UTC format, such as 2019-01-07T15:00:00Z.
        :type StreamEndTime: str
        :param StopReason: Stop reason.
        :type StopReason: str
        :param Duration: Push duration in seconds.
        :type Duration: int
        :param ClientIp: Host IP.
        :type ClientIp: str
        :param Resolution: Resolution.
        :type Resolution: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None
        self.StreamStartTime = None
        self.StreamEndTime = None
        self.StopReason = None
        self.Duration = None
        self.ClientIp = None
        self.Resolution = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        self.StreamStartTime = params.get("StreamStartTime")
        self.StreamEndTime = params.get("StreamEndTime")
        self.StopReason = params.get("StopReason")
        self.Duration = params.get("Duration")
        self.ClientIp = params.get("ClientIp")
        self.Resolution = params.get("Resolution")


class StreamName(AbstractModel):
    """Stream name list.

    """

    def __init__(self):
        """
        :param StreamName: Stream name.
        :type StreamName: str
        :param AppName: Application name.
        :type AppName: str
        :param DomainName: Push domain name.
        :type DomainName: str
        :param StreamStartTime: Push start time.
In UTC format, such as 2019-01-07T12:00:00Z.
        :type StreamStartTime: str
        :param StreamEndTime: Push end time.
In UTC format, such as 2019-01-07T15:00:00Z.
        :type StreamEndTime: str
        :param StopReason: Stop reason.
        :type StopReason: str
        :param Duration: Push duration in seconds.
        :type Duration: int
        :param ClientIp: Host IP.
        :type ClientIp: str
        :param Resolution: Resolution.
        :type Resolution: str
        """
        self.StreamName = None
        self.AppName = None
        self.DomainName = None
        self.StreamStartTime = None
        self.StreamEndTime = None
        self.StopReason = None
        self.Duration = None
        self.ClientIp = None
        self.Resolution = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamStartTime = params.get("StreamStartTime")
        self.StreamEndTime = params.get("StreamEndTime")
        self.StopReason = params.get("StopReason")
        self.Duration = params.get("Duration")
        self.ClientIp = params.get("ClientIp")
        self.Resolution = params.get("Resolution")


class StreamOnlineInfo(AbstractModel):
    """Queries active push information

    """

    def __init__(self):
        """
        :param StreamName: Stream name.
        :type StreamName: str
        :param PublishTimeList: Push time list
        :type PublishTimeList: list of PublishTime
        :param AppName: Application name.
        :type AppName: str
        :param DomainName: Push domain name.
        :type DomainName: str
        """
        self.StreamName = None
        self.PublishTimeList = None
        self.AppName = None
        self.DomainName = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        if params.get("PublishTimeList") is not None:
            self.PublishTimeList = []
            for item in params.get("PublishTimeList"):
                obj = PublishTime()
                obj._deserialize(item)
                self.PublishTimeList.append(obj)
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")


class TemplateInfo(AbstractModel):
    """Transcoding template information.

    """

    def __init__(self):
        """
        :param Vcodec: Video encoding format:
h264/h265.
        :type Vcodec: str
        :param VideoBitrate: Video bitrate. Value range: 100–8000 Kbps.
        :type VideoBitrate: int
        :param Acodec: Audio codec. Valid values: aac, mp3.
        :type Acodec: str
        :param AudioBitrate: Audio bitrate. Value range: 0–500 Kbps.
        :type AudioBitrate: int
        :param Width: Width. Value range: 0–3000.
        :type Width: int
        :param Height: Height. Value range: 0–3000.
        :type Height: int
        :param Fps: Frame rate. Value range: 0–200 FPS.
        :type Fps: int
        :param Gop: Keyframe interval. Value range: 1–50s.
        :type Gop: int
        :param Rotate: Rotation angle. Valid values: 0, 90, 180, 270.
        :type Rotate: int
        :param Profile: Encoding quality. Valid values:
baseline, main, high.
        :type Profile: str
        :param BitrateToOrig: Whether to not exceed the original bitrate. 0: no; 1: yes.
        :type BitrateToOrig: int
        :param HeightToOrig: Whether to not exceed the original height. 0: no; 1: yes.
        :type HeightToOrig: int
        :param FpsToOrig: Whether to not exceed the original frame rate. 0: no; 1: yes.
        :type FpsToOrig: int
        :param NeedVideo: Whether to keep the video. 0: no; 1: yes.
        :type NeedVideo: int
        :param NeedAudio: Whether to keep the audio. 0: no; 1: yes.
        :type NeedAudio: int
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param TemplateName: Template name.
        :type TemplateName: str
        :param Description: Template description.
        :type Description: str
        :param AiTransCode: Whether it is a top speed codec template. 0: no, 1: yes. Default value: 0.
        :type AiTransCode: int
        :param AdaptBitratePercent: `VideoBitrate` minus top speed codec bitrate. Value range: 0.1–0.5.
        :type AdaptBitratePercent: float
        """
        self.Vcodec = None
        self.VideoBitrate = None
        self.Acodec = None
        self.AudioBitrate = None
        self.Width = None
        self.Height = None
        self.Fps = None
        self.Gop = None
        self.Rotate = None
        self.Profile = None
        self.BitrateToOrig = None
        self.HeightToOrig = None
        self.FpsToOrig = None
        self.NeedVideo = None
        self.NeedAudio = None
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.AiTransCode = None
        self.AdaptBitratePercent = None


    def _deserialize(self, params):
        self.Vcodec = params.get("Vcodec")
        self.VideoBitrate = params.get("VideoBitrate")
        self.Acodec = params.get("Acodec")
        self.AudioBitrate = params.get("AudioBitrate")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        self.Gop = params.get("Gop")
        self.Rotate = params.get("Rotate")
        self.Profile = params.get("Profile")
        self.BitrateToOrig = params.get("BitrateToOrig")
        self.HeightToOrig = params.get("HeightToOrig")
        self.FpsToOrig = params.get("FpsToOrig")
        self.NeedVideo = params.get("NeedVideo")
        self.NeedAudio = params.get("NeedAudio")
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.AiTransCode = params.get("AiTransCode")
        self.AdaptBitratePercent = params.get("AdaptBitratePercent")


class UnBindLiveDomainCertRequest(AbstractModel):
    """UnBindLiveDomainCert request structure.

    """

    def __init__(self):
        """
        :param DomainName: Playback domain name.
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")


class UnBindLiveDomainCertResponse(AbstractModel):
    """UnBindLiveDomainCert response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateLiveWatermarkRequest(AbstractModel):
    """UpdateLiveWatermark request structure.

    """

    def __init__(self):
        """
        :param WatermarkId: Watermark ID.
Get the watermark ID in the returned value of the [AddLiveWatermark](/document/product/267/30154) API call.
        :type WatermarkId: int
        :param PictureUrl: Watermark image URL.
        :type PictureUrl: str
        :param XPosition: Display position: X-axis offset. Default value: 0.
        :type XPosition: int
        :param YPosition: Display position: Y-axis offset. Default value: 0.
        :type YPosition: int
        :param WatermarkName: Watermark name.
        :type WatermarkName: str
        :param Width: Watermark width or its percentage of the live streaming video width. It is recommended to just specify either height or width as the other will be scaled proportionally to avoid distortions. The original width is used by default.
        :type Width: int
        :param Height: Watermark height or its percentage of the live streaming video width. It is recommended to just specify either height or width as the other will be scaled proportionally to avoid distortions. The original height is used by default.
        :type Height: int
        """
        self.WatermarkId = None
        self.PictureUrl = None
        self.XPosition = None
        self.YPosition = None
        self.WatermarkName = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        self.PictureUrl = params.get("PictureUrl")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        self.WatermarkName = params.get("WatermarkName")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class UpdateLiveWatermarkResponse(AbstractModel):
    """UpdateLiveWatermark response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class WatermarkInfo(AbstractModel):
    """Watermark information.

    """

    def __init__(self):
        """
        :param WatermarkId: Watermark ID.
        :type WatermarkId: int
        :param PictureUrl: Watermark image URL.
        :type PictureUrl: str
        :param XPosition: Display position: X-axis offset.
        :type XPosition: int
        :param YPosition: Display position: Y-axis offset.
        :type YPosition: int
        :param WatermarkName: Watermark name.
        :type WatermarkName: str
        :param Status: Current status. 0: not used. 1: in use.
        :type Status: int
        :param CreateTime: Creation time.
        :type CreateTime: str
        :param Width: Watermark width.
        :type Width: int
        :param Height: Watermark height.
        :type Height: int
        """
        self.WatermarkId = None
        self.PictureUrl = None
        self.XPosition = None
        self.YPosition = None
        self.WatermarkName = None
        self.Status = None
        self.CreateTime = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        self.PictureUrl = params.get("PictureUrl")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        self.WatermarkName = params.get("WatermarkName")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.Width = params.get("Width")
        self.Height = params.get("Height")