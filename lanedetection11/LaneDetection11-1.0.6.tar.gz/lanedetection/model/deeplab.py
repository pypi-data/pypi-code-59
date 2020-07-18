import torch
import torch.nn as nn
import torch.nn.functional as F
from .resnet import ResNet101
from .aspp import build_aspp
from .decoder import build_decoder
from .batchnorm import SynchronizedBatchNorm2d

class DeepLab(nn.Module):
    def __init__(self, backbone='resnet', output_stride=16, num_classes=21,
                 sync_bn=True, freeze_bn=False):
        super(DeepLab, self).__init__()
        if backbone == 'drn':
            output_stride = 8

        if sync_bn == True:
            BatchNorm = SynchronizedBatchNorm2d
        else:
            BatchNorm = nn.BatchNorm2d

        self.backbone = ResNet101(output_stride, BatchNorm)
        self.aspp = build_aspp(backbone, output_stride, BatchNorm)
        self.decoder = build_decoder(num_classes, backbone, BatchNorm)

        self.freeze_bn = freeze_bn

    def forward(self, input):
        x, low_level_feat = self.backbone(input)
        x = self.aspp(x)
        x = self.decoder(x , low_level_feat)
        x = F.interpolate(x , size=input.size()[2:], mode='bilinear', align_corners=True)

        return x

    def freeze_bn(self):
        for m in self.modules():
            if isinstance(m, SynchronizedBatchNorm2d):
                m.eval()
            elif isinstance(m, nn.BatchNorm2d):
                m.eval()

    def get_1x_lr_params(self):
        modules = [self.backbone]
        for i in range(len(modules)):
            for m in modules[i].named_modules():
                if self.freeze_bn:
                    if isinstance(m[1], nn.Conv2d):
                        for p in m[1].parameters():
                            if p.requires_grad:
                                yield p
                else:
                    if isinstance(m[1], nn.Conv2d) or isinstance(m[1], SynchronizedBatchNorm2d) \
                            or isinstance(m[1], nn.BatchNorm2d):
                        for p in m[1].parameters():
                            if p.requires_grad:
                                yield p

    def get_10x_lr_params(self):
        modules = [self.aspp, self.decoder]
        for i in range(len(modules)):
            for m in modules[i].named_modules():
                if self.freeze_bn:
                    if isinstance(m[1], nn.Conv2d):
                        for p in m[1].parameters():
                            if p.requires_grad:
                                yield p
                else:
                    if isinstance(m[1], nn.Conv2d) or isinstance(m[1], SynchronizedBatchNorm2d) \
                            or isinstance(m[1], nn.BatchNorm2d):
                        for p in m[1].parameters():
                            if p.requires_grad:
                                yield p

# if __name__ == "__main__":
#     model = DeepLab(sync_bn=True)
#     model.load_state_dict(torch.load('deeplab-resnet101.pth.tar')['state_dict'])
#     model.eval()
#     from PIL import Image
#     import matplotlib.pyplot as plt
#     from torchvision import transforms
#
#     input_image = Image.open('test.jpg')
#     # input_image = input_image.resize((256,256))
#     plt.imshow(input_image)
#     plt.show()
#     # input = torch.rand(1, 3, 513, 513)
#     # output = model(input)
#     # print(output.size())
#
#     preprocess = transforms.Compose([
#         transforms.ToTensor(),
#         transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
#     ])
#
#     input_tensor = preprocess(input_image)
#     input_batch = input_tensor.unsqueeze(0)  # create a mini-batch as expected by the model
#
#     # move the input and model to GPU for speed if available
#     if torch.cuda.is_available():
#         input_batch = input_batch.to('cuda')
#         model.to('cuda')
#
#     model.eval()
#     with torch.no_grad():
#         # output = model(input_batch)['out'][0]
#         output = model(input_batch)
#         output = output[0]
#         # output = model.forward(input_batch)
#         # print(output.size())
#         # print(output)
#
#     # plt.imshow(output[0, :])
#     # plt.show()
#     output_predictions = output.argmax(0)
#     # print(output_predictions)
#     # print(output.argmax(0).size())
#     # output_predictions = output_predictions[0]
#
#     # create a color pallette, selecting a color for each class
#     palette = torch.tensor([2 ** 25 - 1, 2 ** 15 - 1, 2 ** 21 - 1])
#     colors = torch.as_tensor([i for i in range(21)])[:, None] * palette
#     colors = (colors % 255).numpy().astype("uint8")
#
#     # plot the semantic segmentation predictions of 21 classes in each color
#     r = Image.fromarray(output_predictions.byte().cpu().numpy()).resize(input_image.size)
#     r.putpalette(colors)
#     # print(r)
#     # import matplotlib.pyplot as plt
#     plt.imshow(r)
#     plt.show()
