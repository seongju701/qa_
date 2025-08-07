from .base_page import BasePage

class HomePage(BasePage):
    def click_login_button(self):
        self.page.get_by_role("button", name="로그인").click()

    def click_signup_link(self):
        self.page.get_by_role("link", name="회원가입").click()

    def search_lecture(self, keyword):
        self.page.get_by_role("combobox", name="나의 진짜 성장을 도와줄 실무 강의를 찾아보세요").fill(keyword)
        self.page.get_by_role("button", name="인프런 통합 검색").click()