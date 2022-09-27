from timm.models import xcit
from timm.models.registry import register_model

from robustbench.model_zoo.architectures.dm_wide_resnet import CIFAR10_MEAN, CIFAR10_STD, CIFAR100_MEAN, CIFAR100_STD

from .utils_architectures import normalize_timm_model

default_cfgs = {
    'debenedetti2020light_xcit_s_imagenet_linf':
    xcit._cfg(
        url=
        "https://github.com/RobustBench/robustbench/releases/download/v1.1/debenedetti2022light-xcit-s-imagenet-linf.pth.tar"
    ),
    'debenedetti2020light_xcit_s_cifar10_linf':
    xcit._cfg(
        url=
        "https://github.com/RobustBench/robustbench/releases/download/v1.1/debenedetti2022light-xcit-s-cifar10-linf.pth.tar",
        input_size=(3, 32, 32),
        mean=CIFAR10_MEAN,
        std=CIFAR10_STD),
    'debenedetti2020light_xcit_s_cifar100_linf':
    xcit._cfg(
        url=
        "https://github.com/RobustBench/robustbench/releases/download/v1.1/debenedetti2022light-xcit-s-cifar100-linf.pth.tar",
        input_size=(3, 32, 32),
        mean=CIFAR100_MEAN,
        std=CIFAR100_STD),
    'debenedetti2020light_xcit_m_cifar10_linf':
    xcit._cfg(
        url=
        "https://github.com/RobustBench/robustbench/releases/download/v1.1/debenedetti2022light-xcit-m-cifar10-linf.pth.tar",
        input_size=(3, 32, 32),
        mean=CIFAR10_MEAN,
        std=CIFAR10_STD),
    'debenedetti2020light_xcit_m_cifar100_linf':
    xcit._cfg(
        url=
        "https://github.com/RobustBench/robustbench/releases/download/v1.1/debenedetti2022light-xcit-m-cifar100-linf.pth.tar",
        input_size=(3, 32, 32),
        mean=CIFAR100_MEAN,
        std=CIFAR100_STD),
    'debenedetti2020light_xcit_m_imagenet_linf':
    xcit._cfg(
        url=
        "https://github.com/RobustBench/robustbench/releases/download/v1.1/debenedetti2022light-xcit-m-imagenet-linf.pth.tar"
    ),
    'debenedetti2020light_xcit_l_cifar10_linf':
    xcit._cfg(
        url=
        "https://github.com/RobustBench/robustbench/releases/download/v1.1/debenedetti2022light-xcit-l-cifar10-linf.pth.tar",
        input_size=(3, 32, 32),
        mean=CIFAR10_MEAN,
        std=CIFAR10_STD),
    'debenedetti2020light_xcit_l_cifar100_linf':
    xcit._cfg(
        url=
        "https://github.com/RobustBench/robustbench/releases/download/v1.1/debenedetti2022light-xcit-l-cifar100-linf.pth.tar",
        input_size=(3, 32, 32),
        mean=CIFAR100_MEAN,
        std=CIFAR100_STD),
    'debenedetti2020light_xcit_l_imagenet_linf':
    xcit._cfg(
        url=
        "https://github.com/RobustBench/robustbench/releases/download/v1.1/debenedetti2022light-xcit-l-imagenet-linf.pth.tar"
    ),
}


def adapt_model_patches(model: xcit.XCiT, new_patch_size: int):
    to_divide = model.patch_embed.patch_size / new_patch_size
    assert int(
        to_divide
    ) == to_divide, "The new patch size should divide the original patch size"
    to_divide = int(to_divide)
    assert to_divide % 2 == 0, "The ratio between the original patch size and the new patch size should be divisible by 2"
    for conv_index in range(0, to_divide, 2):
        model.patch_embed.proj[conv_index][0].stride = (1, 1)  # type: ignore
    model.patch_embed.patch_size = new_patch_size
    return model


@register_model
def debenedetti2020light_xcit_s_imagenet_linf(pretrained=False, **kwargs):
    model_kwargs = dict(patch_size=16,
                        embed_dim=384,
                        depth=12,
                        num_heads=8,
                        eta=1.0,
                        tokens_norm=True,
                        **kwargs)
    model = xcit._create_xcit('debenedetti2020light_xcit_s_imagenet_linf',
                              pretrained=pretrained,
                              **model_kwargs)
    assert isinstance(model, xcit.XCiT)
    model = normalize_timm_model(model)
    return model


@register_model
def debenedetti2020light_xcit_m_imagenet_linf(pretrained=False, **kwargs):
    model_kwargs = dict(patch_size=16,
                        embed_dim=512,
                        depth=12,
                        num_heads=8,
                        eta=1.0,
                        tokens_norm=True,
                        **kwargs)
    model = xcit._create_xcit('debenedetti2020light_xcit_m_imagenet_linf',
                              pretrained=pretrained,
                              **model_kwargs)
    assert isinstance(model, xcit.XCiT)
    model = normalize_timm_model(model)
    return model


@register_model
def debenedetti2020light_xcit_l_imagenet_linf(pretrained=False, **kwargs):
    model_kwargs = dict(patch_size=16,
                        embed_dim=768,
                        depth=12,
                        num_heads=16,
                        eta=1.0,
                        tokens_norm=True,
                        **kwargs)
    model = xcit._create_xcit('debenedetti2020light_xcit_l_imagenet_linf',
                              pretrained=pretrained,
                              **model_kwargs)
    assert isinstance(model, xcit.XCiT)
    model = normalize_timm_model(model)
    return model


@register_model
def debenedetti2020light_xcit_s_cifar10_linf(pretrained=False, **kwargs):
    model_kwargs = dict(
        patch_size=16,  # 16 because the pre-trained model has 16
        embed_dim=384,
        depth=12,
        num_heads=8,
        eta=1.0,
        tokens_norm=True,
        **kwargs)
    model = xcit._create_xcit('debenedetti2020light_xcit_s_cifar10_linf',
                              pretrained=pretrained,
                              **model_kwargs)
    assert isinstance(model, xcit.XCiT)
    model = adapt_model_patches(model, 4)
    model = normalize_timm_model(model)
    return model


@register_model
def debenedetti2020light_xcit_s_cifar100_linf(pretrained=False, **kwargs):
    model_kwargs = dict(
        patch_size=16,  # 16 because the pre-trained model has 16
        embed_dim=384,
        depth=12,
        num_heads=8,
        eta=1.0,
        tokens_norm=True,
        **kwargs)
    model = xcit._create_xcit('debenedetti2020light_xcit_s_cifar100_linf',
                              pretrained=pretrained,
                              **model_kwargs)
    assert isinstance(model, xcit.XCiT)
    model = adapt_model_patches(model, 4)
    model = normalize_timm_model(model)
    return model


@register_model
def debenedetti2020light_xcit_m_cifar10_linf(pretrained=False, **kwargs):
    model_kwargs = dict(
        patch_size=16,  # 16 because the pre-trained model has 16
        embed_dim=512,
        depth=12,
        num_heads=8,
        eta=1.0,
        tokens_norm=True,
        **kwargs)
    model = xcit._create_xcit('debenedetti2020light_xcit_m_cifar10_linf',
                              pretrained=pretrained,
                              **model_kwargs)
    assert isinstance(model, xcit.XCiT)
    model = adapt_model_patches(model, 4)
    model = normalize_timm_model(model)
    return model


@register_model
def debenedetti2020light_xcit_m_cifar100_linf(pretrained=False, **kwargs):
    model_kwargs = dict(
        patch_size=16,  # 16 because the pre-trained model has 16
        embed_dim=512,
        depth=12,
        num_heads=8,
        eta=1.0,
        tokens_norm=True,
        **kwargs)
    model = xcit._create_xcit('debenedetti2020light_xcit_m_cifar100_linf',
                              pretrained=pretrained,
                              **model_kwargs)
    assert isinstance(model, xcit.XCiT)
    model = adapt_model_patches(model, 4)
    model = normalize_timm_model(model)
    return model


@register_model
def debenedetti2020light_xcit_l_cifar10_linf(pretrained=False, **kwargs):
    model_kwargs = dict(
        patch_size=16,  # 16 because the pre-trained model has 16
        embed_dim=768,
        depth=12,
        num_heads=16,
        eta=1.0,
        tokens_norm=True,
        **kwargs)
    model = xcit._create_xcit('debenedetti2020light_xcit_l_cifar10_linf',
                              pretrained=pretrained,
                              **model_kwargs)
    assert isinstance(model, xcit.XCiT)
    model = adapt_model_patches(model, 4)
    model = normalize_timm_model(model)
    return model


@register_model
def debenedetti2020light_xcit_l_cifar100_linf(pretrained=False, **kwargs):
    model_kwargs = dict(
        patch_size=16,  # 16 because the pre-trained model has 16
        embed_dim=768,
        depth=12,
        num_heads=16,
        eta=1.0,
        tokens_norm=True,
        **kwargs)
    model = xcit._create_xcit('debenedetti2020light_xcit_l_cifar100_linf',
                              pretrained=pretrained,
                              **model_kwargs)
    assert isinstance(model, xcit.XCiT)
    model = adapt_model_patches(model, 4)
    model = normalize_timm_model(model)
    return model
