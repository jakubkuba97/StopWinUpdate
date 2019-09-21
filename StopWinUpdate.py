"""
    Stop windows update and disable it
"""


def stop_services(services: list, disable_startup: bool = True) -> None:
    import win32serviceutil

    print('Number of services: %i' % len(services))
    print('Stopping services...')
    for service in services:
        print()
        try:
            if win32serviceutil.QueryServiceStatus(service[0])[1] == 4:
                win32serviceutil.StopService(service[0])
                print('%s stopped.' % service[1])
            else:
                print('%s was already stopped.' % service[1])
        except:
            print('\tCould not stop service %s!' % service[1])
        if disable_startup:
            try:
                win32serviceutil.ChangeServiceConfig(None, serviceName=service[0], startType='disabled', delayedstart=None)
                print('%s startup settings changed.' % service[1])
            except:
                print('\tCould not change settings of service %s!' % service[1])
                if service[1] == 'Update Orchestrator Service':
                    print('\tThis is an expected behaviour.')
    print('\nFinished stopping services.')


if __name__ == '__main__':
    names = [['UsoSvc', 'Update Orchestrator Service'],
             ['wuauserv', 'Windows Update']]
    stop_services(names)
    input()
