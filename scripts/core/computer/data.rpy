default computer.data.anon.pos = {'egy': (325, 20)}
default computer.data.jenny.pos = {}


init 1 python in computer.user:

    anon = User('anon', '[firstname]',
                _('{#passwd}cookies'), _('{#hint}Sticky'))

    apps = anon.apps
    apps.add('bin', _('Recycle Bin'), 'pc_app_dir', 'fo3', 'nl3', 'lsh')
    apps.add('fo3', _('Failout 3'))
    apps.add('nl3', _('Never-Life 3'))
    apps.add('lsh', _('Leisure Suit Harold'))
    apps.add('pic', _('Photos'), 'pc_app_dir', 'im1', 'im2')
    apps.add('im1', _('class'), 'pc_app_jpg', 'class', icon='jpg')
    apps.add('im2', _('GT420'), 'pc_app_jpg', 'car', icon='jpg')
    apps.add('sts', _('Summertime SAGA'), 'pc_app_saga', hook='saga')
    apps.add('rdc', _('Remote Access'), action=Call('pc.connect', 'jenny'))
    apps.add('wrk', _('Homework'), icon='doc', action=Jump('pc_homework'))
    apps.add('mzr', _('Maze Runner'), action=Jump('pc_maze'))
    apps.add('egy', _('eGay'), 'pc_app_egay', hook='egay')

    apps.root = ('bin', 'pic', 'sts', 'rdc', 'wrk', 'mzr', 'egy')


    jenny = User('jenny', 'xX~HOTKITTY69~Xx',
                 _('{#passwd}badmonster'), _("{#hint}What's my favorite toy?"))

    apps = jenny.apps
    apps.add('bin', _('Recycle Bin'), 'pc_app_dir', 'im1'),
    apps.add('im1', _('cam_shot_372'), 'pc_app_jpg', 'cam', icon='jpg', hook='nude'),
    apps.add('pic', _('Photos'), 'pc_app_dir', 'new', 'im4', 'im5'),
    apps.add('new', _('New Folder'), 'pc_app_dir', 'im2', 'im3', icon='dir'),
    apps.add('im2', _('pixx1'), 'pc_app_jpg', 'pix', icon='jpg', hook='swim'),
    apps.add('im3', _('selfie!'), 'pc_app_jpg', 'selfie', icon='jpg'),
    apps.add('im4', _('Old_pic'), 'pc_app_jpg', 'jane', icon='jpg', hook='jane'),
    apps.add('im5', _('Fam_015'), 'pc_app_jpg', 'family', icon='jpg', hook='loss'),
    apps.add('sts', _('Summertime SAGA'), 'pc_app_saga', hook='saga'),
    apps.add('wsh', _('Wish List'), 'pc_app_wish', icon='doc', hook='wish'),
    apps.add('cam', _('CAMslut'), 'pc_app_camslut', hook='camslut'),
    apps.add('eml', _('Outlood Express'), 'pc_app_email', hook='mail')

    apps.root = ('bin', 'pic', 'sts', 'wsh', 'cam', 'eml')

    mail = jenny.mail
    mail.add('twt', _('Twatter <pablo69@sagamail.dc>'),
                    _('Pablo69 wants to share a picture with you!'),
                    1527843960, att=True)
    mail.add('cam', _('CAMslut <stats@camslut.dc>'),
                    _('Your earnings for this month'),
                    1527838440)
    mail.add('toy', _('LewdToys <shipping@lewdtoys.dc>'),
                    _('Your item(s) have been shipped!'),
                    1527595200, att=True)
    mail.add('ptv', _('Pink Channel <subscription@pink.dc>'),
                    _('Thank you for subscribing!'),
                    1527163200, hook='pink')
    mail.add('419', _('Kaosu Uzu <kaoprince11@afromail.dc>'),
                    _('I am Nigeria Prince, in needs of assistance!'),
                    1527076800)
    mail.add('beg', _('TheTittyShit <tit@theshit.dc>'),
                    _('send nudes'),
                    1526119200)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
