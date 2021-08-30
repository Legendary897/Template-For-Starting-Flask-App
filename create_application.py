from flask import Flask
from flask_assets import Environment
from flask_cors import CORS
from backend_modules.development_tools.bundler_frontend import BundleFrontend
from backend_modules.routing.login_manage.login_server import atmosphere_login
from backend_modules.routing.configure_test import application_routing
from cheroot.wsgi import Server as WSGIServer


class CreatorApplication(object):

    def __init__(self):
        self.application = Flask(__name__, template_folder='/templates', static_folder='/static')
        self.debug = None
        self.reloader = None
        self.host = None
        self.port = None

    def _create_app(self):
        self.application.config["SECRET_KEY"] = 'secret!'
        cors = CORS(self.application, resources={r"/foo": {"origins": "*"}})
        assets = Environment(self.application)
        assets.url = self.application.static_url_path
        js, scss = BundleFrontend().js_and_scss_bundle()
        assets.register("scss_all", scss)
        assets.register("js_all", scss)

        self.application.config.from_object('settings')
        atmosphere_login(self.application)
        self.application.register_blueprint(application_routing)
        self.debug = self.application.config.get('DEBUG', False)
        self.reloader = self.application.config.get('RELOADER', False)
        self.host = self.application.config.get('HOST')
        self.port = self.application.config.get('PORT')
        with open("routing.dat", "w") as file:
            for i in self.application.url_map.iter_rules():
                file.writelines(str(i) + "\n")
        with open("methods_routing.dat", "w") as file:
            for i in self.application.url_map.iter_rules():
                file.writelines(str(i.endpoint) + "\n")

    def start_app(self):
        self._create_app()
        self.application.run(
            use_reloader=self.reloader,
            debug=self.debug,
            threaded=True,
            host=self.host,
            port=self.port
        )

        # server = WSGIServer(bind_addr=("0.0.0.0", 2001), wsgi_app=self.application, numthreads=100)
        # try:
        #     server.start()
        # except KeyboardInterrupt:
        #     server.stop()
