from core.application_builder import ApplicationBuilder

from assets.scripts.layers.game_layer import GameLayer


if __name__ == "__main__":
    ApplicationBuilder() \
        .use_layer(GameLayer) \
        .with_title("Box Down") \
        .with_resolution((900, 600)).build().run()
