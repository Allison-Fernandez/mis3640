import time
epoch = time.time()
epoch_minutes = epoch / 60
epoch_hours = epoch_minutes / 60
epoch_days = epoch_hours / 24
print(time.localtime())
print('{:.1f} days since the epoch.'.format(epoch_days))