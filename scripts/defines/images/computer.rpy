image pc_monitor = Fixed(Solid('000', xysize=(1024, 125)),
                         Solid('000', xysize=(90, 768)),
                         Solid('000', xysize=(1024, 115), yalign=1.),
                         Solid('000', xysize=(90, 768), xalign=1.))


image pc_monitor_anon = ConditionSwitch(
    'game.timer.is_dark()', 'computer/pc_monitor_anon_night.png',
    'True', 'computer/pc_monitor_anon_day.png')

image pc_monitor_jenny = ConditionSwitch(
    'game.timer.is_night()', 'computer/pc_monitor_jenny_night.png',
    'game.timer.is_evening()', 'computer/pc_monitor_jenny_evening.png',
    'True', 'computer/pc_monitor_jenny_day.png')


image pc_sticky_idle = ConditionSwitch(
    'game.timer.is_dark()', 'computer/pc_sticky_night.png',
    'True', 'computer/pc_sticky_day.png')
image pc_sticky_over = ConditionSwitch(
    'game.timer.is_dark()', im.MatrixColor(
        'computer/pc_sticky_night.png', over),
    'True', im.MatrixColor('computer/pc_sticky_day.png', over))


image pc_sys_exit_idle = 'computer/pc_sys_exit.png'
image pc_sys_exit_over = im.MatrixColor('computer/pc_sys_exit.png', over)
image pc_sys_halt_idle = 'computer/pc_sys_halt.png'
image pc_sys_halt_over = im.MatrixColor('computer/pc_sys_halt.png', over)
image pc_sys_quit_idle = 'computer/pc_sys_quit.png'
image pc_sys_quit_over = im.MatrixColor('computer/pc_sys_quit.png', over)


image pc_window_close_idle = 'computer/pc_window_close.png'
image pc_window_close_over = im.MatrixColor(
    'computer/pc_window_close.png', over)


image pc_icon_bin_idle = 'computer/pc_icon_bin.png'
image pc_icon_bin_over = im.MatrixColor('computer/pc_icon_bin.png', over)
image pc_icon_cam_idle = 'computer/pc_icon_cam.png'
image pc_icon_cam_over = im.MatrixColor('computer/pc_icon_cam.png', over)
image pc_icon_dir_idle = 'computer/pc_icon_dir.png'
image pc_icon_dir_over = im.MatrixColor('computer/pc_icon_dir.png', over)
image pc_icon_doc_idle = 'computer/pc_icon_doc.png'
image pc_icon_doc_over = im.MatrixColor('computer/pc_icon_doc.png', over)
image pc_icon_egy_idle = 'computer/pc_icon_egy.png'
image pc_icon_egy_over = im.MatrixColor('computer/pc_icon_egy.png', over)
image pc_icon_eml_idle = 'computer/pc_icon_eml.png'
image pc_icon_eml_over = im.MatrixColor('computer/pc_icon_eml.png', over)
image pc_icon_fo3_idle = 'computer/pc_icon_fo3.png'
image pc_icon_fo3_over = im.MatrixColor('computer/pc_icon_fo3.png', over)
image pc_icon_jpg_idle = 'computer/pc_icon_jpg.png'
image pc_icon_jpg_over = im.MatrixColor('computer/pc_icon_jpg.png', over)
image pc_icon_lsh_idle = 'computer/pc_icon_lsh.png'
image pc_icon_lsh_over = im.MatrixColor('computer/pc_icon_lsh.png', over)
image pc_icon_mzr_idle = 'computer/pc_icon_mzr.png'
image pc_icon_mzr_over = im.MatrixColor('computer/pc_icon_mzr.png', over)
image pc_icon_nl3_idle = 'computer/pc_icon_nl3.png'
image pc_icon_nl3_over = im.MatrixColor('computer/pc_icon_nl3.png', over)
image pc_icon_pic_idle = 'computer/pc_icon_pic.png'
image pc_icon_pic_over = im.MatrixColor('computer/pc_icon_pic.png', over)
image pc_icon_rdc_idle = 'computer/pc_icon_rdc.png'
image pc_icon_rdc_over = im.MatrixColor('computer/pc_icon_rdc.png', over)
image pc_icon_sts_idle = 'computer/pc_icon_sts.png'
image pc_icon_sts_over = im.MatrixColor('computer/pc_icon_sts.png', over)


image pc_camslut_button_over = Frame(
    im.MatrixColor('computer/pc_camslut_button.png',
                   im.matrix.tint(.2, .6, .2)), 50, 5, 5, 6)
image pc_camslut_button_idle = Frame(
    'computer/pc_camslut_button.png', 50, 5, 5, 6)
image pc_camslut_button_live = Frame(
    im.MatrixColor('computer/pc_camslut_button.png',
                   im.matrix.tint(.6, .2, .2)), 50, 5, 5, 6)
image pc_camslut_video_bm_idle = 'computer/pc_camslut_video_bm.png'
image pc_camslut_video_bm_over = im.MatrixColor(
    'computer/pc_camslut_video_bm.png', over)
image pc_camslut_video_ec_idle = 'computer/pc_camslut_video_ec.png'
image pc_camslut_video_ec_over = im.MatrixColor(
    'computer/pc_camslut_video_ec.png', over)
image pc_camslut_video_uv_idle = 'computer/pc_camslut_video_uv.png'
image pc_camslut_video_uv_over = im.MatrixColor(
    'computer/pc_camslut_video_uv.png', over)

image pc_egay_body = Frame('computer/pc_egay_body.png', 3, 0, 3, 0)
image pc_egay_buy_idle = Frame('computer/pc_egay_buy.png', 5, 7, 5, 7)
image pc_egay_buy_over = Frame(
    im.MatrixColor('computer/pc_egay_buy.png', over), 5, 7, 5, 7)
image pc_egay_head = Frame('computer/pc_egay_head.png', 4, 4, 4, 4)

image pc_email_over = Frame(
    im.MatrixColor('computer/pc_email_unread.png',
                   over * im.matrix.tint(.8, .85, 1)), 5, 5, 5, 5)
image pc_email_read = Frame('computer/pc_email_read.png', 5, 5, 5, 5)
image pc_email_unread = Frame('computer/pc_email_unread.png', 5, 5, 5, 5)

image pc_note_mistake = Transform('computer/pc_note_mistake.png', yoffset=2)

image pc_saga_menu = Fixed('pc_saga_menu_static',
                           Movie(play='computer/pc_saga_menu.mkv'))
image pc_saga_splash:
    Solid('0b0d17')
    'computer/pc_saga_splash.png' with Dissolve(1.5)

image pc_web_url = Frame('computer/pc_web_url.png', 63, 3, 85, 3, ysize=30)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
