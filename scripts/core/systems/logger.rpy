init -999 python hide:
    '''
    This is intended primarily for debugging during development, but can
    also be useful when assisting users. Log file creation is attempted
    alongside saves, and fails safe when this is not possible.
    '''

    from logging import DEBUG, FileHandler, Formatter, StreamHandler, getLogger
    from os.path import join


    store.logger = log = getLogger()

    if len(log.handlers) == 0:
        log.setLevel(DEBUG)
        
        datefmt = '%Y-%m-%d %H:%M:%S'
        fmt = '%(asctime)s.%(msecs)03d  %(levelname)-8s %(message)s'
        
        if config.developer or persistent._console_log:
            sh = StreamHandler()
            sh.setFormatter(Formatter(datefmt=datefmt[9:], fmt=fmt))
            log.addHandler(sh)
        
        paths = (join(config.savedir, 'saga.log'),
                 join(config.gamedir, 'saves', 'saga.log'))
        
        for path in paths:
            try:
                fh = FileHandler(path)
                fh.setFormatter(Formatter(datefmt=datefmt, fmt=fmt))
                log.debug('logging to %s', path)
                log.addHandler(fh)
                break
            except IOError as e:
                log.warning('unable to log to %s', path)
                log.warning(e)
        
        log.debug('logger configured')

    log.info('log begins')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
