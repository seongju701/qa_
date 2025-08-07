from .base_page import BasePage

class LoginPage(BasePage):
    def login_with_kakao(self, username, password):
        self.page.get_by_role("button", name="카카오로 로그인").click()
        self.page.get_by_role("textbox", name="계정정보 입력").click()
        self.page.get_by_role("textbox", name="계정정보 입력").fill(username)
        self.page.get_by_role("textbox", name="비밀번호 입력").click()
        self.page.get_by_role("textbox", name="비밀번호 입력").fill(password)
        self.page.get_by_role("button", name="로그인", exact=True).click()

    def go_to_user_dashboard(self):
        self.page.get_by_role("button", name="사용자 대시보드 페이지로 이동").click()

    def get_dashboard_name(self):
        return self.page.get_by_role("link", name="유저 대시보드로 이동").inner_text()