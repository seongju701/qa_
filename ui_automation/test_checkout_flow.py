# pytest -v -rA --html=report.html


# 1. 회원가입
def test_create_id(page):
    page.get_by_role("button", name="로그인").click()
    page.get_by_role("link", name="회원가입").click()
    page.get_by_role("textbox", name="이메일").click()
    page.get_by_role("textbox", name="이메일").fill("seongju701@naver.com")
    page.get_by_role("textbox", name="비밀번호", exact=True).click()
    page.get_by_role("textbox", name="비밀번호", exact=True).fill("-")
    page.get_by_role("textbox", name="비밀번호 확인").click()
    page.get_by_role("textbox", name="비밀번호 확인").fill("-")
# 2. 로그인
def test_login(page):
    page.get_by_role("button", name="로그인").click()
    page.get_by_role("button", name="카카오로 로그인").click()
    page.get_by_role("textbox", name="계정정보 입력").click()
    page.get_by_role("textbox", name="계정정보 입력").fill("seongju701@naver.com")
    page.get_by_role("textbox", name="비밀번호 입력").click()
    page.get_by_role("textbox", name="비밀번호 입력").fill("-")
    page.get_by_role("button", name="로그인", exact=True).click()
    page.get_by_role("button", name="사용자 대시보드 페이지로 이동").click()
    name = page.get_by_role("link", name="유저 대시보드로 이동").inner_text()
    assert name in "조성주"

# 3. 강의검색
def test_lecture_search(page):
    page.get_by_role("combobox", name="나의 진짜 성장을 도와줄 실무 강의를 찾아보세요").fill("python")
    page.get_by_role("button", name="인프런 통합 검색").click()
    p_text = page.get_by_role("link").filter(has_text="프로그래밍 시작하기 : 파이썬 입문 (Inflearn") \
        .locator("p").first.inner_text()
    assert p_text in "[100%]프로그래밍 시작하기 : 파이썬 입문 (Inflearn Original)"

# 4. 장바구니 담기
def test_search_class(page):
    page.get_by_role("button", name="로그인").click()
    page.get_by_role("button", name="카카오로 로그인").click()
    page.get_by_role("textbox", name="계정정보 입력").click()
    page.get_by_role("textbox", name="계정정보 입력").fill("seongju701@naver.com")
    page.get_by_role("textbox", name="비밀번호 입력").click()
    page.get_by_role("textbox", name="비밀번호 입력").fill("-")
    page.get_by_role("button", name="로그인", exact=True).click()
    page.get_by_role("combobox", name="나의 진짜 성장을 도와줄 실무 강의를 찾아보세요").fill("python")
    page.get_by_role("button", name="인프런 통합 검색").click()
    page.locator(".css-8o8bso.mantine-1avyp1d").first.hover()
    with page.expect_popup() as page1_info:
        page.locator("#course-hover-card").get_by_text("이미 2").click()
    page1 = page1_info.value
    page1.get_by_role("link", name="수강 바구니로 이동").click()
    lecture = page1.get_by_role("link", name="프로그래밍 시작하기 : 파이썬 입문 (Inflearn Original)", exact=True).inner_text()
    assert lecture in "[100%]프로그래밍 시작하기 : 파이썬 입문 (Inflearn Original)"

#결제하기
def test_payment(page):
    page.get_by_role("button", name="로그인").click()
    page.get_by_role("button", name="카카오로 로그인").click()
    page.get_by_role("textbox", name="계정정보 입력").click()
    page.get_by_role("textbox", name="계정정보 입력").fill("seongju701@naver.com")
    page.get_by_role("textbox", name="비밀번호 입력").click()
    page.get_by_role("textbox", name="비밀번호 입력").fill("-")
    page.get_by_role("button", name="로그인", exact=True).click()
    page.get_by_role("combobox", name="나의 진짜 성장을 도와줄 실무 강의를 찾아보세요").fill("python")
    page.get_by_role("button", name="인프런 통합 검색").click()
    page.locator(".css-8o8bso.mantine-1avyp1d").first.hover()
    with page.expect_popup() as page1_info:
        page.locator("#course-hover-card").get_by_text("이미 2").click()
    page1 = page1_info.value
    page1.get_by_role("link", name="수강 바구니로 이동").click()
    page1.locator("#__next > div.css-1e8gneg.mantine-1fr50if > div.css-c31z9o.mantine-1jggmkl > main > div > div > div.css-sycckr.mantine-lixs2r > div > div.mantine-Stack-root.css-1i1jy58.mantine-1yopscp > div.mantine-Stack-root.css-1vf0mqh.mantine-1178y6y > div > button").click()
    page1.get_by_role("textbox", name="아이디 또는 전화번호").click()
    page1.get_by_role("textbox", name="아이디 또는 전화번호").fill("seongju701")
    page1.get_by_role("textbox", name="비밀번호").click()
    page1.get_by_role("textbox", name="비밀번호").fill("-!")
    page1.get_by_role("button", name="로그인").click()