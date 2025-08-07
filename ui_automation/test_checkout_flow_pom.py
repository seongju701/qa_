import pytest
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from pages.lecture_page import LecturePage
from pages.cart_page import CartPage

@pytest.mark.order(1)
def test_create_id(page):
    home = HomePage(page)
    signup = SignupPage(page)
    home.click_login_button()
    home.click_signup_link()
    signup.fill_email("seongju701@naver.com")
    signup.fill_password("whtjdwn1")
    signup.fill_password_confirm("whtjdwn1")

@pytest.mark.order(2)
def test_login(page):
    home = HomePage(page)
    login = LoginPage(page)
    home.click_login_button()
    login.login_with_kakao("seongju701@naver.com", "whtjdwn1")
    login.go_to_user_dashboard()
    name = login.get_dashboard_name()
    assert "조성주" in name

@pytest.mark.order(3)
def test_lecture_search(page):
    home = HomePage(page)
    lecture = LecturePage(page)
    home.search_lecture("python")
    p_text = lecture.get_first_search_result_text()
    assert "[100%]프로그래밍 시작하기 : 파이썬 입문 (Inflearn Original)" in p_text

@pytest.mark.order(4)
def test_search_class(page):
    home = HomePage(page)
    login = LoginPage(page)
    lecture = LecturePage(page)
    cart = CartPage(page)

    # 로그인
    home.click_login_button()
    login.login_with_kakao("seongju701@naver.com", "whtjdwn1")

    # 강의 검색 및 장바구니 담기
    home.search_lecture("python")
    lecture.hover_first_lecture()
    popup_page = lecture.click_enroll_popup()

    cart = CartPage(popup_page)
    cart.go_to_cart()
    lecture_title = cart.get_lecture_title()
    assert "[100%]프로그래밍 시작하기 : 파이썬 입문 (Inflearn Original)" in lecture_title

@pytest.mark.order(5)
def test_payment(page):
    home = HomePage(page)
    login = LoginPage(page)
    lecture = LecturePage(page)
    cart = CartPage(page)

    # 로그인
    home.click_login_button()
    login.login_with_kakao("seongju701@naver.com", "-")

    # 강의 검색 및 장바구니 담기
    home.search_lecture("python")
    lecture.hover_first_lecture()
    popup_page = lecture.click_enroll_popup()

    cart = CartPage(popup_page)
    cart.go_to_cart()
    cart.click_payment_button()
    cart.fill_payment_id("seongju701")
    cart.fill_payment_password("-")
    cart.click_payment_login()