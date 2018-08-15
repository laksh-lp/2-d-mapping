import gps, os, time

session = gps.gps()

while 1:
    os.system('clear')
    #session.query('admosy') 
    # a = altitude, d = date/time, m=mode,  
    # o=postion/fix, s=status, y=satellites

    print
    print ' GPS reading'
    print '----------------------------------------'
    print 'latitude    ' , session.fix.latitude
    print 'longitude   ' , session.fix.longitude
    print 'altitude    ' , session.fix.altitude
    #print 'heading     ' , session.fix.heading
    time.sleep(3)
