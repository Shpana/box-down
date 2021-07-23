from core.application_context import ApplicationContext

from assets.scripts.layers.game_layer import GameLayer


if __name__ == "__main__":
    context = ApplicationContext()
    context.config.from_ini("project.config")

    app = context.get_instance()
    app.add_layer(GameLayer(context))
    app.run()
