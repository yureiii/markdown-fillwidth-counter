from markdown_fillwidth_counter import count_fullwidth_text


def test_count_fullwidth_text():
    assert count_fullwidth_text("abcあいう") == 3
    assert count_fullwidth_text("3 文字") == 2
    assert count_fullwidth_text("（　）") == 3
    assert count_fullwidth_text("<ruby>漢字<rt>かんじ</rt></ruby>") == 2
    assert count_fullwidth_text("# 見出し\n 本文") == 2
    assert count_fullwidth_text("<!-- コメントアウトした文字は数えない -->") == 0
    text = """# サンプル文章
これはテスト<ruby>用<rt>よう</rt></ruby>の文章です．43 文字になることを想定しています．
全角の文字は数えます．（　）

<!-- コメントアウトした文字は数えない -->

## 記号
! @ # $ % ^ & * ( ) - _ = + [ ] { } \\ | ; : ' " , < . > / ? ` ~
"""

    assert count_fullwidth_text(text) == 43
