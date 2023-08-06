from python_anticaptcha import AnticaptchaClient, ImageToTextTask

class Labrar:
    # ... [resto de la clase]
    
    def resolver_captcha(self, captcha_image_path):
        api_key = 'TU_API_KEY'
        client = AnticaptchaClient(api_key)
        task = ImageToTextTask(captcha_image_path)
        job = client.createTask(task)
        job.join()
        return job.get_captcha_text()
