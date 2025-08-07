from .base_page import BasePage

class CartPage(BasePage):
    def go_to_cart(self):
        self.page.get_by_role("link", name="수강 바구니로 이동").click()

    def get_lecture_title(self):
        return self.page.get_by_role("link", name="프로그래밍 시작하기 : 파이썬 입문 (Inflearn Original)", exact=True).inner_text()

    def click_payment_button(self):
        self.page.locator("#__next > div.css-1e8gneg.mantine-1fr50if > div.css-c31z9o.mantine-1jggmkl > main > div > div > div.css-sycckr.mantine-lixs2r > div > div.mantine-Stack-root.css-1i1jy58.mantine-1yopscp > div.mantine-Stack-root.css-1vf0mqh.mantine-1178y6y > div > button").click()

    def fill_payment_id(self, user_id):
        self.page.get_by_role("textbox", name="아이디 또는 전화번호").click()
        self.page.get_by_role("textbox", name="아이디 또는 전화번호").fill(user_id)

    def fill_payment_password(self, password):
        self.page.get_by_role("textbox", name="비밀번호").click()
        self.page.get_by_role("textbox", name="비밀번호").fill(password)

    def click_payment_login(self):
        self.page.get_by_role("button", name="로그인").click()