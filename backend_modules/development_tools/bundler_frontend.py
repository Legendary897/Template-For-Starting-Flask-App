from flask_assets import Bundle


class BundleFrontend(object):

    @staticmethod
    def js_and_scss_bundle():
        # Перечислить все js файлы, указать аргумент output куда сохранять bundle
        js = Bundle()
        # Необходимо иметь файл index.scss
        scss = Bundle("css/index.scss", filters="pyscss", output="all.css")
        return js, scss
