a
    /i<b?
  ?                   @   s?   d dl Z d dlZd dlmZmZmZmZ d dlZd dlZd dl	T d dl
Zd dlZd dlZd dlmZ e?? Zej?e?Ze?? ZdZdd? Zdd	? Zd
d? Ze?  dS )?    N)?run?Popen?PIPE?STDOUT)?*)?PathzBy Saohy; Telegram: @Saohyc                  C   s?  t ?d dddd?} | ?? t jkr,t??  ?nb| ?? }tjdt	j
dd? tjtj?|?d t	jdd? tttt?? ??d	???d
k ?rtjdt	jddt	jd?}t|?? ?d
k r?q?q?|dv r?d?tjtjdd??}td|? d?dd? t??  ?q?q?|dv r?t??  ?q?q?n?t ?d dddd?}|?? t jk?r4t??  nZ|?? }tjdt	j
dd? tjtj?|?d t	jdd? td|? d|? d?dd? t??  d S )NZAPK?.? zAPK files (*.apk)|*.apkz
[App]: r   ??interval?
z
*.keystore?   z-Key file not found, you want create it? y/n >F?r   Zhide_cursorZinput_color)?y?YZyesZYes?
   ??k?keytool -genkey -v -keystore ?>.keystore -keyalg RSA -keysize 2048 -validity 10000 -alias appT??shell)?n?NZnoZNoZKEYSTOREz&KEYSTORE files (*.keystore)|*.keystorez[Key]: z

zAjarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore ? z app)?guiZ
FileDialogZ	ShowModalZ	ID_CANCEL?sys?exitZGetPath?Write?Print?ColorsZgreen?os?path?basenameZwhite?len?listr   ?getcwd?glob?InputZgreen_to_red?	light_red?strip?join?random?sample?string?ascii_lettersr   )?fileZpathA?user?name?keyZpathk? r4   ?mangerAPK.py?Sign   s4     
r6   c                  C   sj   t ?  tjdtjddtjd?} t| ?? ?dk rFd?t	j
tjdd??} n | } td	| ? d
?dd? t??  d S )NzFile name?: ?{?G?z??Fr   r   r	   r   r   r   r   Tr   )?printr   r(   r    Zblue_to_greenr)   r$   r*   r+   r,   r-   r.   r/   r   r   r   )r2   r4   r4   r5   ?Key4   s    r9   c                  C   sl   t ?  tjdtjdd? tjdtjdd? tjdtjddtjd?} | ?? dv rVt	?  n| ?? d	v rht
?  d S )
Nz[1/A] Sign an apk
r7   r
   z[2/B] Create key
z
Select an option >Fr   )?1?A)?2?B)r8   r   r   r    Zgreen_to_bluer(   Zpurple_to_bluer)   ?upperr6   r9   )r1   r4   r4   r5   ?main?   s    r?   )r,   r.   ?
subprocessr   r   r   r   r!   r   ZpystyleZshutilZslZrequestsZwxr   ?pathlibr   r&   ?homer"   r#   ?__file__Zapp_nameZApp?coreZ__license__r6   r9   r?   r4   r4   r4   r5   ?<module>   s"   !
