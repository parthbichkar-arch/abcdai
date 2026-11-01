def towerofhanoi(n,fromrod,torod,auxrod):
    if n==0:
        return

    towerofhanoi(n-1,fromrod,auxrod,torod)

    towerofhanoi("Disk",n,"moved from rod",fromrod,"to rod",torod)

    towerofhanoi(n-1,auxrod,torod,fromrod)

    if  __name__ == "__main__":
        n=3
   

        towerofhanoi(n,'A','C','B')