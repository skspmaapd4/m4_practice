
from datetime import date
import itertools
import threading
import time
import sys

# For ID Registration-------------
students_id = list(range(1000000))
num_of_stud = len(students_id)


class election():
    # Candidates for Member of parliament----------------------------------
    p1_no = 1
    p2_no = 2
    p3_no = 3
    p1_name = "MD DILSHAD ALAM"
    p2_name = "PREMALATHA B.T"
    p3_name = "INAMDAR"
    pres_1 = 0
    pres_2 = 0
    pres_3 = 0
    # Candidates for Munciple corporation ----------------------------------
    vp1_no = 1
    vp2_no = 2
    vp3_no = 3
    vp1_name = "SWATHI"
    vp2_name = "PUSHPALATHA B.T"
    vp3_name = "IMRAN"
    vpres_1 = 0
    vpres_2 = 0
    vpres_3 = 0
    # Candidates for Secretary----------------------------------
    sec1_no = 1
    sec2_no = 2
    sec3_no = 3
    sec1_name = "PUSHPALATHA B.T"
    sec2_name = "IMRAN"
    sec3_name = "MD DILSHAD ALAM"
    sec_1 = 0
    sec_2 = 0
    sec_3 = 0
    # Candidates for panchayat----------------------------------
    aud1_no = 1
    aud2_no = 2
    aud3_no = 3
    aud1_name = "TANYA "
    aud2_name = "KUMAR"
    aud3_name = "SUSIL"
    aud_1 = 0
    aud_2 = 0
    aud_3 = 0
    # Candidates for sarpanch----------------------------------
    tre1_no = 1
    tre2_no = 2
    tre3_no = 3
    tre1_name = "MR SIVA"
    tre2_name = "IMRAN"
    tre3_name = "SWATHI"
    tre_1 = 0
    tre_2 = 0
    tre_3 = 0
    # Candidates for chairman----------------------------------
    media1_no = 1
    media2_no = 2
    media3_no = 3
    media1_name = "ANSARI "
    media2_name = "KARTIK"
    media3_name = "ROBIN"
    media_1 = 0
    media_2 = 0
    media_3 = 0
    # Candidates for ward council----------------------------------
    f_rep1_no = 1
    f_rep2_no = 2
    f_rep3_no = 3
    f_rep1_name = "NIDHI"
    f_rep2_name = "PRITHVI"
    f_rep3_name = "BHARAT "
    f_rep_1 = 0
    f_rep_2 = 0
    f_rep_3 = 0
    # Candidates for zila panchayat---------------------------------
    s_rep1_no = 1
    s_rep2_no = 2
    s_rep3_no = 3
    s_rep1_name = "TANYA"
    s_rep2_name = "PRITHVI"
    s_rep3_name = "NIRMAL"
    s_rep_1 = 0
    s_rep_2 = 0
    s_rep_3 = 0
    # Candidates for student union----------------------------------
    t_rep1_no = 1
    t_rep2_no = 2
    t_rep3_no = 3
    t_rep1_name = "SRINIDHI "
    t_rep2_name = "ANSARI"
    t_rep3_name = "ROBIN"
    t_rep_1 = 0
    t_rep_2 = 0
    t_rep_3 = 0
    # Candidates for Member of the lagislative Assembly----------------------------------
    frt_rep1_no = 1
    frt_rep2_no = 2
    frt_rep3_no = 3
    frt_rep1_name = "MD DILSHAD ALAM"
    frt_rep2_name = "NIRMAL"
    frt_rep3_name = "SUSHIL KUMAR"
    frt_rep_1 = 0
    frt_rep_2 = 0
    frt_rep_3 = 0