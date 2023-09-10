from pynopegl_utils.misc import SceneCfg, scene

import pynopegl as ngl


@scene()
def overlay(cfg: SceneCfg):
    image = next(m for m in cfg.medias if m.filename.endswith(".jpg"))
    overlay = next(m for m in cfg.medias if m.filename.endswith(".png"))

    cfg.aspect_ratio = image.width, image.height

    bg_tex = ngl.Texture2D(data_src=ngl.Media(image.filename))
    bg = ngl.RenderTexture(bg_tex)

    fg_tex = ngl.Texture2D(data_src=ngl.Media(overlay.filename))
    fg = ngl.RenderTexture(fg_tex)
    fg.set_blending("src_over")

    fg.add_filters(
        # A PNG is usually not premultiplied, but the blending operator expects
        # it to be.
        ngl.FilterPremult(),
        # Make the overlay half opaque
        ngl.FilterOpacity(0.5),
    )

    return ngl.Group(children=[bg, fg])
