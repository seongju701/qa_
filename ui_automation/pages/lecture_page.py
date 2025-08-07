from .base_page import BasePage

class LecturePage(BasePage):
    def get_first_search_result_text(self):
        p_text = self.page.get_by_role("link").filter(has_text="프로그래밍 시작하기 : 파이썬 입문 (Inflearn") \
            .locator("p").first.inner_text()
        return p_text

    def hover_first_lecture(self):
        self.page.locator(".css-8o8bso.mantine-1avyp1d").first.hover()

    def click_enroll_popup(self):
        with self.page.expect_popup() as popup_info:
            self.page.locator("#course-hover-card").get_by_text("이미 2").click()
        return popup_info.value