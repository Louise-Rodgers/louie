from seleniumbase import SB
with SB(uc=True, test=True) as louie:

    if True:
        url = "https://kick.com/brutalles"
        louie.uc_open_with_reconnect(url, 5)
        louie.uc_gui_click_captcha()
        louie.sleep(1)
        louie.uc_gui_handle_captcha()
        louie.sleep(1)
        if louie.is_element_present('button:contains("Accept")'):
            louie.uc_click('button:contains("Accept")', reconnect_time=4)
        if louie.is_element_visible('#injected-channel-player'):
            louie2 = louie.get_new_driver(undetectable=True)
            louie2.uc_open_with_reconnect(url, 5)
            louie2.uc_gui_click_captcha()
            louie2.uc_gui_handle_captcha()
            louie.sleep(10)
            if louie2.is_element_present('button:contains("Accept")'):
                louie2.uc_click('button:contains("Accept")', reconnect_time=4)
            while louie.is_element_visible('#injected-channel-player'):
                louie.sleep(10)
            louie.quit_extra_driver()
    louie.sleep(1)
