from .base_page import BasePage

class SignupPage(BasePage):
    def fill_email(self, email):
        self.page.get_by_role("textbox", name="이메일").click()
        self.page.get_by_role("textbox", name="이메일").fill(email)

    def fill_password(self, pw):
        self.page.get_by_role("textbox", name="비밀번호", exact=True).click()
        self.page.get_by_role("textbox", name="비밀번호", exact=True).fill(pw)

    def fill_password_confirm(self, pw):
        self.page.get_by_role("textbox", name="비밀번호 확인").click()
        self.page.get_by_role("textbox", name="비밀번호 확인").fill(pw)