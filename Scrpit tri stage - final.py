import re
import csv
import pandas as pd
from pandas import DataFrame
import numpy as np
import openpyxl

#-----------------------------------------------------------------------------#

df = pd.read_excel(r'D:\Utilisateurs\Ali\OneDrive\Bureau\Travail lycée\Terminale\NSI\Stage\JungleBikeArticleTriangle.xlsx')
libelle_list = df['Libellé'].tolist()

df2 = pd.read_excel(r'D:\Utilisateurs\Ali\OneDrive\Bureau\Travail lycée\Terminale\NSI\Stage\JungleBikeArticleTriangle.xlsx')
code_bar_list = df2['Code barre'].tolist()

df3 = pd.read_csv(r"D:\Utilisateurs\Ali\OneDrive\Bureau\Travail lycée\Terminale\NSI\Stage\Libellé.csv")
libelle_list_test = df3["Libellé"].tolist()

df4 = pd.read_excel(r'D:\Utilisateurs\Ali\OneDrive\Bureau\Travail lycée\Terminale\NSI\Stage\JungleBikeArticleTriangle.xlsx')
code_art_list = df4["Code sous-famille article"].tolist()

code_art_libelle_list = [code_art_list,libelle_list]

df_couleurs = pd.read_excel(r"D:\Utilisateurs\Ali\OneDrive\Bureau\Travail lycée\Terminale\NSI\Stage\Ref_liste_couleurs_V3.xlsx")
couleurs_list = df_couleurs["REF_NUANCE_FR"].tolist()

#-----------------------------------------------------------------------------#
'''
#libelle_string = ";\n".join(libelle_list)
#diametre_string = ";".join(diametre_list[0])


for n in range(1840):
    print(diametre(regex2,n))

def elt_liste(libelle_list,n):
    return libelle_list[n]
'''
#-----------------------------------------------------------------------------#
#AUTONOMY
re_auto = r'.* ([0-9]+[h]).*'
def autonomy(re_auto,n):
    global output_auto_str
    output_auto = re.split(re_auto,libelle_list[n])
    if len(output_auto) >= 0:
        del output_auto[0]
    if len(output_auto) >= 1:
        del output_auto[1]
    output_auto_str = "".join(output_auto)
    return output_auto_str

autonomy_list = [autonomy(re_auto,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#BAR
re_bar = r".* ([0-9]+bar).*"
def bar(re_bar,n):
    global output_bar_str
    output_bar = re.split(re_bar,libelle_list[n])
    if len(output_bar) >= 0:
        del output_bar[0]
    if len(output_bar) >= 1:
        del output_bar[1]
    output_bar_str = "".join(output_bar)
    return output_bar_str

bar_list = [bar(re_bar,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#BIKE_NB
re_vide = r".*[^\n]"
def vide(re_vide,n):
    global output_vide_str
    output_vide = re.split(re_vide,libelle_list[n])
    for i in range(2):
        del output_vide[0]
    output_vide_str = "".join(output_vide)
    return output_vide_str

vide_list = [vide(re_vide,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#CAPACITY
re_capacity = r".* ([0-9., ]+[mMlL][^mM]).*"
def capacity(re_capacity,n):
    global output_capacity_str
    global output_capacity
    output_capacity = re.split(re_capacity,libelle_list[n])
    if len(output_capacity) >= 0:
        del output_capacity[0]
    if len(output_capacity) >= 1:
        del output_capacity[1]
    output_capacity_str = "".join(output_capacity)
    return output_capacity_str

capacity_list = [capacity(re_capacity,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#COMPATIBILITY_REF
re_compa_ref = r".* ([0-9]+Ref).*"
def compatibility_ref(re_compa_ref,n):
    global output_compa_ref_str
    output_compa_ref = re.split(re_compa_ref,libelle_list[n])
    if len(output_compa_ref) >= 0:
        del output_compa_ref[0]
    if len(output_compa_ref) >= 1:
        del output_compa_ref[1]
    output_compa_ref_str = "".join(output_compa_ref)
    return output_compa_ref_str

compatibility_ref_list = [compatibility_ref(re_compa_ref,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#DIAM_AXE
regex2_1 = r".* ([0-9., ]+[cmCM][^lL]).*" #Sert à trouver le diamètre en cm ou mm
def diametre_axe(regex2_1,n):
    global output_rex2_1_str
    global output_rex2_1
    if code_art_libelle_list[0][n] == 'M_ROUES':
        output_rex2_1 = re.split(regex2_1,libelle_list[n])
        if len(output_rex2_1) >= 0:
            del output_rex2_1[0]
        if len(output_rex2_1) >= 1:
            del output_rex2_1[1]
    else:
        output_rex2_1 = ""
    output_rex2_1_str = "".join(output_rex2_1)
    return output_rex2_1_str

diametre_axe_list = [diametre_axe(regex2_1,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#DIAMETER
regex2 = r".* ([0-9., ]+[cmCM][^lL]).*" #Sert à trouver le diamètre en cm ou mm
def diametre(regex2,n):
    global output_rex2_str
    if code_art_libelle_list[0][n] == 'M_ROUES':
        output_rex2 = re.split(regex2,libelle_list[n])
        if len(output_rex2) >= 0:
            del output_rex2[0]
        if len(output_rex2) >= 1:
            del output_rex2[1]
    else:
        output_rex2 = ""
    output_rex2_str = "".join(output_rex2)
    return output_rex2_str

diametre_list = [diametre(regex2,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#DIM_TEMP
regex_dim_temp = r".* ([0-9.,x\/ ]+[x\/][0-9]+[cm][^lL]).*" #Sert à trouver le diamètre en cm ou mm
def dim_temp(regex_dim_temp,n):
    global output_rex_dim_temp_str
    output_rex2 = re.split(regex_dim_temp,libelle_list[n])
    if len(output_rex2) >= 0:
        del output_rex2[0]
    if len(output_rex2) >= 1:
        del output_rex2[1]
    output_rex_dim_temp_str = "".join(output_rex2)
    return output_rex_dim_temp_str

dim_temp_list = [dim_temp(regex_dim_temp,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#EAN13
re_ean13 = r"([0-9]{12,13}).*"
def ean13(re_ean13,n):
    global output_ean13
    output_ean13 = re.split(re_ean13,code_bar_list[n])
    if len(output_ean13) >= 0:
        del output_ean13[0]
    if len(output_ean13) >= 1:
        del output_ean13[1]
    if not output_ean13 == []:
        if len(output_ean13[0]) < len('1234567891234'):
            output_ean13[0] = "0" + output_ean13[0]
    '''output_ean13_str = "".join(output_ean13) NE MARCHE PAS !'''
    return output_ean13

ean13_list = [ean13(re_ean13,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#ENTRAXE
re_entraxe = r".* ([0-9., ]+[mM][^lL]).*"
def entraxe(re_entraxe,n):
    global output_entraxe_str
    global output_entraxe
    if code_art_libelle_list[0][n] == 'M_PLATEAUX':
        output_entraxe = re.split(re_entraxe,libelle_list[n])
        if len(output_entraxe) >= 0:
            del output_entraxe[0]
        if len(output_entraxe) >= 1:
            del output_entraxe[1]
    else:
        output_entraxe = ""
    output_entraxe_str = "".join(output_entraxe)
    return output_entraxe_str

entraxe_list = [entraxe(re_entraxe,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#FIXATION_INCLUDED
re_non = r".*[^\n]"
def non(re_non,n):
    return 'non'

non_list = [non(re_non,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#FIXATION_ON
re_vide = r".*[^\n]"
def vide(re_vide,n):
    global output_vide_str
    output_vide = re.split(re_vide,libelle_list[n])
    for i in range(2):
        del output_vide[0]
    output_vide_str = "".join(output_vide)
    return output_vide_str

vide_list = [vide(re_vide,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#FUNCTION_NB
re_vide = r".*[^\n]"
def un(re_vide,n):
    global output_un_str
    global output_un
    output_un = re.split(re_vide,libelle_list[n])
    for i in range(2):
        del output_un[0]
    output_un = ["1"]
    output_un_str = "".join(output_un)
    return output_un_str

un_list = [un(re_vide,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#HEIGHT
regex_height = r".* ([0-9., ]+[cm][^lL]).*" #Sert à trouver le diamètre en cm ou mm
def height(regex_height,n):
    global output_rex_height_str
    if code_art_libelle_list[0][n] != 'C_PNEUS':
        output_rex2 = re.split(regex_height,libelle_list[n])
        if len(output_rex2) >= 0:
            del output_rex2[0]
        if len(output_rex2) >= 1:
            del output_rex2[1]
    else:
        output_rex2 = [""]
    output_rex_height_str = "".join(output_rex2)
    return output_rex_height_str

height_list = [height(regex_height,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#LENGTH
regex_len = r".* ([0-9., ]+[cm]+)( [length]+)?.*" #Sert à trouver le diamètre en cm ou mm
def length(regex_len,n):
    global output_rex_len_str
    if code_art_libelle_list[0][n] == 'D_CINTRES' or code_art_libelle_list[0][n] =='K_FLEX' or code_art_libelle_list[0][n] =='K_CABLES' or code_art_libelle_list[0][n] =='M_VALVES':
        output_len = re.split(regex_len,libelle_list[n])
        if len(output_len) >= 0:
            del output_len[0]
        if len(output_len) >= 2:
            del output_len[2]
        if len(output_len) >= 1:
            if output_len[1] == None:
                del output_len[1]
    else:
        output_len = ""
    output_rex_len_str = "".join(output_len)
    return output_rex_len_str

len_list = [length(regex_len,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#LUMEN
re_lumen = r".* ([0-9]+ Lux).*"
def lumen(re_lumen,n):
    global output_lumen_str
    output_lumen = re.split(re_lumen,libelle_list[n])
    if len(output_lumen) >= 0:
        del output_lumen[0]
    if len(output_lumen) >= 1:
        del output_lumen[1]
    output_lumen_str = "".join(output_lumen)
    return output_lumen_str

lumen_list = [lumen(re_lumen,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#MODELE
''''''
re_model1 = r"^([a-zA-Zîâéàèùïüë ]+-?[0-9]?[^0-9Tpi])" # regex à essayer
re_model2 = r"^[a-zA-Zîâéàèùïüë \/]+-?[0-9]?[^0-9Tpi]([0-9.,]?[a-zA-Zîâéàèùïüë \/]+)"
re_mod_100 = r"Zero100 ([0-9.,]?[a-zA-Zîâéàèùïüë \/]+)"
re_mod_1 = r"^Zero1 ([0-9.,]?[a-zA-Zîâéàèùïüë \/]+)"
re_mod_2 = r"^Zero2 ([0-9.,]?[a-zA-Zîâéàèùïüë \/]+)"
re_mod_35 = r"^([0-9a-zA-Zîâéàèùïüë ]+[\/][\w]+)"
def modele(re_model1,re_model2,re_mod_100,re_mod_1,re_mod_2,re_mod_35,n):
    global output_rex3_str_1
    global output_rex3_str_2
    global output_rex_3_1
    global output_rex3_2
    global output_rex3_mod_100_str
    global output_rex3_mod_1_str
    global output_rex3_mod_2_str
    global output_rex3_mod_2
    global output_35
    global output_35_str
    #---------------------------------------------------------#
    output_rex3_1 = re.split(re_model1,libelle_list[n])
    output_rex3_2 = re.split(re_model2,libelle_list[n])
    output_rex3_mod_100 = re.split(re_mod_100,libelle_list[n])
    output_rex3_mod_1 = re.split(re_mod_1,libelle_list[n])
    output_rex3_mod_2 = re.split(re_mod_2,libelle_list[n])
    output_35 = re.split(re_mod_35,libelle_list[n])
    #---------------------------------------------------------#
    if len(output_rex3_1) == 0:
        output_rex3_1 = output_rex3_1
    if len(output_rex3_1) > 1:
        del output_rex3_1[0]
    if len(output_rex3_1) > 1:
        del output_rex3_1[1]
    #-----------------------------------#
    if len(output_rex3_2) == 0:
        output_rex3_2 = output_rex3_2
    if len(output_rex3_2) > 1:
        del output_rex3_2[0]
    if len(output_rex3_2) > 1:
        del output_rex3_2[1]
    #-----------------------------------#
    if len(output_rex3_mod_100) == 0:
        output_rex3_mod_100 = output_rex3_mod_100
    if len(output_rex3_mod_100) > 1:
        del output_rex3_mod_100[0]
    if len(output_rex3_mod_100) > 1:
        del output_rex3_mod_100[1]
    #-----------------------------------#
    if len(output_rex3_mod_1) == 0:
        output_rex3_mod_1 = output_rex3_mod_1
    if len(output_rex3_mod_1) > 1:
        del output_rex3_mod_1[0]
    if len(output_rex3_mod_1) > 1:
        del output_rex3_mod_1[1]
    #-----------------------------------#
    if len(output_rex3_mod_2) == 0:
        output_rex3_mod_2 = output_rex3_mod_2
    if len(output_rex3_mod_2) > 1:
        del output_rex3_mod_2[0]
    if len(output_rex3_mod_2) > 1:
        del output_rex3_mod_2[1]
    #---------------------------------------------------------#
    if len(output_35) == 0:
        output_35 = output_35
    if len(output_35) > 1:
        del output_35[0]
    if len(output_35) > 1:
        del output_35[1]
    #---------------------------------------------------------#
    output_rex3_str_1 = "".join(output_rex3_1)
    output_rex3_str_2 = "".join(output_rex3_2)
    output_rex3_mod_100_str = "".join(output_rex3_mod_100)
    output_rex3_mod_1_str = "".join(output_rex3_mod_1)
    output_rex3_mod_2_str = "".join(output_rex3_mod_2)
    output_35_str = "".join(output_35)
    #---------------------------------------------------------#
    output_rex3_mod_100_str = output_rex3_mod_100_str.replace(' ','')
    #---------------------------------------------------------#
    if code_art_libelle_list[0][n] == 'M_K7' or code_art_libelle_list[0][n] == 'M_COLSAU' or code_art_libelle_list[0][n] == 'M_COLSEL' or code_art_libelle_list[0][n] == 'M_MEJ':
        output_rex3_str_1 = output_rex3_str_1 + output_rex3_str_2
    else:
        output_rex3_str_1 = output_rex3_str_1
    #---------------------------------------------------------#
    if output_rex3_str_2 == output_rex3_mod_2_str:
        output_rex3_str_1 = output_rex3_str_1 + output_rex3_mod_2_str
    else:
        output_rex3_str_1 = output_rex3_str_1
    #---------------------------------------------------------#
    if output_rex3_str_2 == output_rex3_mod_1_str:
        output_rex3_str_1 = output_rex3_str_1 + output_rex3_mod_1_str
    else:
        output_rex3_str_1 = output_rex3_str_1
    #---------------------------------------------------------#
    if output_rex3_str_1[0] == '3':
        output_rex3_str_1 = output_35_str
    #---------------------------------------------------------#
    return output_rex3_str_1

modele_list = [modele(re_model1,re_model2,re_mod_100,re_mod_1,re_mod_2,re_mod_35,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#PIECE_NB
re_vide = r".*[^\n]"
def un(re_vide,n):
    global output_un_str
    global output_un
    output_un = re.split(re_vide,libelle_list[n])
    for i in range(2):
        del output_un[0]
    output_un = ["1"]
    output_un_str = "".join(output_un)
    return output_un_str

un_list = [un(re_vide,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#PILE_INCLUDED
def pile_inclu(n):
    global output_pile_inclu_str
    if code_art_libelle_list[0][n] == 'K_LIGHT':
        output_pile_inclu_str = 'oui' 
    else:
        output_pile_inclu_str = 'non'
    return output_pile_inclu_str

pile_inclu_list = [pile_inclu(n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#PILE_NB
re_vide = r".*[^\n]"
def vide(re_vide,n):
    global output_vide_str
    output_vide = re.split(re_vide,libelle_list[n])
    for i in range(2):
        del output_vide[0]
    output_vide_str = "".join(output_vide)
    return output_vide_str

vide_list = [vide(re_vide,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#PILE_TYPE
re_vide = r".*[^\n]"
def vide(re_vide,n):
    global output_vide_str
    output_vide = re.split(re_vide,libelle_list[n])
    for i in range(2):
        del output_vide[0]
    output_vide_str = "".join(output_vide)
    return output_vide_str

vide_list = [vide(re_vide,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#PRODUCT_NAME_DECLI
'''VOIR LIGNE 907'''
#-----------------------------------------------------------------------------#
#PRODUCT NAME
''''''
modele_list = [modele(re_model1,re_model2,re_mod_100,re_mod_1,re_mod_2,re_mod_35,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#REGLABLE
def reglable(n):
    global output_reglable_str
    if code_art_libelle_list[0][n] == 'D_ACCES' or code_art_libelle_list[0][n] == 'D_B_ENDS_A' or code_art_libelle_list[0][n] == 'D_BAR_ENDS' or code_art_libelle_list[0][n] == 'D_BIDONS' or code_art_libelle_list[0][n] == 'D_CINTRES' or code_art_libelle_list[0][n] == 'D_COMPTEUR' or code_art_libelle_list[0][n] == 'D_DIRECTIO' or code_art_libelle_list[0][n] == 'D_POTENCES' or code_art_libelle_list[0][n] == 'D_TAPES' or code_art_libelle_list[0][n] == 'D_TDS' or code_art_libelle_list[0][n] == 'D_TT' or code_art_libelle_list[0][n] == 'DC_CADRES' or code_art_libelle_list[0][n] == 'DC_FOURCHE' or code_art_libelle_list[0][n] == 'H_ACCES' or code_art_libelle_list[0][n] == 'SM_ACCES' or code_art_libelle_list[0][n] == 'SM_SELLES':
        output_reglable_str = 'oui' 
    else:
        output_reglable_str = 'non'
    return output_reglable_str

reglable_list = [reglable(n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#RIM_TYPE
re_rim_type = r".*(Carbone).*"
def rim_type(re_rim_type,n):
    global output_rim_type_str
    global output_rim_type
    if code_art_libelle_list[0][n] == 'M_FREINS' or code_art_libelle_list[0][n] == 'M_MEJ':
        output_rim_type = re.split(re_rim_type,libelle_list[n])
        if len(output_rim_type) >= 0:
            del output_rim_type[0]
        if len(output_rim_type) >= 1:
            del output_rim_type[1]
    else:
        output_rim_type = ""
    output_rim_type_str = "".join(output_rim_type)
    return output_rim_type_str

rim_type_list = [rim_type(re_rim_type,n) for n in range(1840)] 

#-----------------------------------------------------------------------------#
#RIM_WIDTH
regex2 = r".* ([0-9., ]+[cm][^lL]).*" #Sert à trouver le diamètre en cm ou mm
def rim_width(regex2,n):
    global output_rim_width_str
    if code_art_libelle_list[0][n] == 'C_PNEUS':
        output_rim_width = re.split(regex2,libelle_list[n])
        if len(output_rim_width) >= 0:
            del output_rim_width[0]
        if len(output_rim_width) >= 1:
            del output_rim_width[1]
    else:
        output_rim_width = ""
    output_rim_width_str = "".join(output_rim_width)
    return output_rim_width_str

rim_width_list = [rim_width(regex2,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#SIZE_GLOBAL
re_size_global = r".*([XSML\/]?[XSML\/]{3}|Small|Medium|Large).*"
def size_global(re_size_global,n):
    global output_size_global_str
    output_size_global = re.split(re_size_global,libelle_list[n])
    if len(output_size_global) >= 0:
        del output_size_global[0]
    if len(output_size_global) >= 1:
        del output_size_global[1]
    output_size_global_str = "".join(output_size_global)
    if output_size_global_str == 'S/S':
        output_size_global_str = 'X' + output_size_global_str
    else:
        output_size_global_str = output_size_global_str
    return output_size_global_str

size_global_list = [size_global(re_size_global,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#SIZE_ID
re_vide = r".*[^\n]"
def zero(re_vide,n):
    global output_zero_str
    global output_zero
    output_zero = re.split(re_vide,libelle_list[n])
    for i in range(2):
        del output_zero[0]
    output_zero = ["0"]
    output_zero_str = "".join(output_zero)
    return output_zero_str

zero_list = [zero(re_vide,n) for n in range(1840)]
    
#-----------------------------------------------------------------------------#
#SIZE_LABEL
re_size_label = r".*([XSML\/]?[XSML\/]{3}|Small|Medium|Large).*"
def size_label(re_size_label,n):
    global output_size_label_str
    output_size_label = re.split(re_size_label,libelle_list[n])
    if len(output_size_label) >= 0:
        del output_size_label[0]
    if len(output_size_label) >= 1:
        del output_size_label[1]
    output_size_label_str = "".join(output_size_label)
    if output_size_label_str == 'S/S':
        output_size_label_str = 'X' + output_size_label_str
    else:
        output_size_label_str = output_size_label_str
    if output_size_label_str == 'Small':
        output_size_label_str = 'S'
    elif output_size_label_str == 'Medium':
        output_size_label_str = 'M'
    elif output_size_label_str == 'Large':
        output_size_label_str = 'L'
    else:
        output_size_label_str = output_size_label_str
    return output_size_label_str

size_label_list = [size_label(re_size_label,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#SPEED_NB
re_speednb = r"([0-9\/]+[vV])" #"([0-9\/]{2}[D])|([0-9\/]{2} dents)"
def speed_nb(re_speednb,n):
    global output_speednb_str
    global output_speednb
    if code_art_libelle_list[0][n] == 'M_PIGNONS' or code_art_libelle_list[0][n] == 'M_PLATEAUX':
        output_speednb = re.split(re_speednb,libelle_list[n])
        if len(output_speednb) >= 0:
            del output_speednb[0]
        if len(output_speednb) >= 1:
            del output_speednb[1]
    else:
        output_speednb = ""
    output_speednb_str = "".join(output_speednb)
    return output_speednb_str

speednb_list = [speed_nb(re_speednb,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#TIGE_SELLE
regex2 = r".* ([0-9., ]+[cm][^lL]).*" #Sert à trouver le diamètre en cm ou mm
def tige(regex2,n):
    global output_tige_str
    global output_tige
    if code_art_libelle_list[0][n] == 'D_TDS' or code_art_libelle_list[0][n] == 'M_TDS':
        output_tige = re.split(regex2,libelle_list[n])
        if len(output_tige) >= 0:
            del output_tige[0]
        if len(output_tige) >= 1:
            del output_tige[1]
    else:
        output_tige = ""
    output_tige_str = "".join(output_tige)
    return output_tige_str

tige_list = [tige(regex2,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#TORX
re_torx = r".* ([0-9., ]+Tx ?[a-z\]?[0-9\/]+).*"
def torx(re_torx,n):
    global output_torx_str
    output_torx = re.split(re_torx,libelle_list[n])
    if len(output_torx) >= 0:
        del output_torx[0]
    if len(output_torx) >= 1:
        del output_torx[1]
    output_torx_str = "".join(output_torx)
    return output_torx_str

torx_list = [torx(re_torx,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#VIS_TYPE
re_vide = r".*[^\n]"
def vide(re_vide,n):
    global output_vide_str
    output_vide = re.split(re_vide,libelle_list[n])
    for i in range(2):
        del output_vide[0]
    output_vide_str = "".join(output_vide)
    return output_vide_str

vide_list = [vide(re_vide,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#VISCOSITY
re_viscosity = r".* ([0-9.,]+wt).*"
def viscosity(re_viscosity,n): 
    global output_viscosity_str
    output_viscosity = re.split(re_viscosity,libelle_list[n])
    if len(output_viscosity) >= 0:
        del output_viscosity[0]
    if len(output_viscosity) >= 1:
        del output_viscosity[1]
    output_viscosity_str = "".join(output_viscosity)
    return output_viscosity_str

viscosity_list = [viscosity(re_viscosity,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#VOLT
re_volt = r".* ([0-9\/]+[vV]).*"
def volt(re_volt,n):
    global output_volt_str
    global output_volt
    if code_art_libelle_list[0][n] == 'B_LIGHT' or code_art_libelle_list[0][n] == 'K_LIGHT':
        output_volt = re.split(re_volt,libelle_list[n])
        if len(output_volt) >= 0:
            del output_volt[0]
        if len(output_volt) >= 1:
            del output_volt[1]
    else:
        output_volt = ""
    output_volt_str = "".join(output_volt)
    return output_volt_str

volt_list = [volt(re_volt,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#WATT
re_watt = r".* ([0-9]+[wW]).*"
def watt(re_watt,n):
    global output_watt_str
    output_watt = re.split(re_watt,libelle_list[n])
    if len(output_watt) >= 0:
        del output_watt[0]
    if len(output_watt) >= 1:
        del output_watt[1]
    output_watt_str = "".join(output_watt)
    return output_watt_str

watt_list = [watt(re_watt,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#WEIGHT
re_weight = r".* ([0-9.,]+[kg]+).*"
def weight(re_weight,n):
    global output_weight_str
    output_weight = re.split(re_weight,libelle_list[n])
    if len(output_weight) >= 0:
        del output_weight[0]
    if len(output_weight) >= 1:
        del output_weight[1]
    output_weight_str = "".join(output_weight)
    return output_weight_str

weight_list = [weight(re_weight,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#WEIGHT_MAX
re_vide = r".*[^\n]"
def vide(re_vide,n):
    global output_vide_str
    output_vide = re.split(re_vide,libelle_list[n])
    for i in range(2):
        del output_vide[0]
    output_vide_str = "".join(output_vide)
    return output_vide_str

vide_list = [vide(re_vide,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#WHEEL_ETRTO
re_wheel_etrto = r".* ([0-9.,x\/ ]+[x\/][0-9]+[cm][^lL]).*"
def wheel_etrto(re_wheel_etrto,n):
    global output_wheel_etrto_str
    global output_wheel_etrto
    if code_art_libelle_list[0][n] == 'C_PNEUS':
        output_wheel_etrto = re.split(re_wheel_etrto,libelle_list[n])
        if len(output_wheel_etrto) >= 0:
            del output_wheel_etrto[0]
        if len(output_wheel_etrto) >= 1:
            del output_wheel_etrto[1]
    else:
        output_wheel_etrto = ""
    output_wheel_etrto_str = "".join(output_wheel_etrto)
    return output_wheel_etrto_str

wheel_etrto_list = [wheel_etrto(re_wheel_etrto, n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#WHEEL_FR
re_wheel_fr = r".*([0-9]?[0-9]{2}x[0-9]+[A-Z])"
def wheel_fr(re_wheel_fr,n):
    global output_wheel_fr_str
    if code_art_libelle_list[0][n] == 'M_ROUES':
        output_wheel_fr = re.split(re_wheel_fr,libelle_list[n]) 
        if len(output_wheel_fr) >= 0:
            del output_wheel_fr[0]
        if len(output_wheel_fr) >= 1:
            del output_wheel_fr[1]
    else:
        output_wheel_fr = ""
    output_wheel_fr_str = "".join(output_wheel_fr)
    return output_wheel_fr_str

wheel_fr_list = [wheel_fr(re_wheel_fr,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#WHEEL_INCH
re_wheel_inch = r".* ([0-9.,\/]+'')(x?[0-9.,\/x]+[']+)?.*"
def wheel_inch(re_wheel_inch,n):
    global output_wheel_inch_str
    if code_art_libelle_list[0][n] == 'M_ROUES':
        output_wheel_inch = re.split(re_wheel_inch,libelle_list[n])
        if len(output_wheel_inch) >= 0:
            del output_wheel_inch[0]
        if len(output_wheel_inch) >= 2:
            del output_wheel_inch[2]
        if len(output_wheel_inch) >= 1:
            if output_wheel_inch[1] == None: 
                del output_wheel_inch[1]
    else:
        output_wheel_inch = ""
    output_wheel_inch_str = "".join(output_wheel_inch)
    return output_wheel_inch_str

wheel_inch_list = [wheel_inch(re_wheel_inch,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#WHEEL_WIDTH
regex2 = r".* ([0-9., ]+[cm][^lL]).*" #Sert à trouver le diamètre en cm ou mm
def wheel_width(regex2,n):
    global output_wheel_width_str
    if code_art_libelle_list[0][n] == 'C_PNEUS':
        output_wheel_width = re.split(regex2,libelle_list[n])
        if len(output_wheel_width) >= 0:
            del output_wheel_width[0]
        if len(output_wheel_width) >= 1:
            del output_wheel_width[1]
    else:
        output_wheel_width = ""
    output_wheel_width_str = "".join(output_wheel_width)
    return output_wheel_width_str

wheel_width_list = [wheel_width(regex2,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#WIDTH
regex2 = r".* ([0-9.,]+[cm][^lL]).*" #Sert à trouver le diamètre en cm ou mm
def diametre(regex2,n):
    global output_rex2_str
    output_rex2 = re.split(regex2,libelle_list[n])
    if len(output_rex2) >= 0:
        del output_rex2[0]
    if len(output_rex2) >= 1:
        del output_rex2[1]
    output_rex2_str = "".join(output_rex2)
    return output_rex2_str

diametre_list = [diametre(regex2,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#COLOR_FR 
re_color_fr = r'.*(Noir|Blanc|Jaune|Bleu|Rouge|Vert|Violet|Rose|Orange|Gris|Marron|Bordeaux|Corail|Turquoise|Kaki|Beige|Doré|Argent|Cuivre|Multicolore|NOIR|BLANC|JAUNE|BLEU|ROUGE|VERT|VIOLET|ROSE|ORANGE|GRIS|MARRON|BORDEAUX|CORAIL|TURQUOISE|KAKI|BEIGE|DORÉ|ARGENT|CUIVRE|MULTICOLORE).*'
def color_fr(re_color_fr,n):
    global output_color_fr_str
    output_color_fr = re.split(re_color_fr,libelle_list[n])
    if len(output_color_fr) >= 0:
        del output_color_fr[0]
    if len(output_color_fr) >= 1:
        del output_color_fr[1]
    output_color_fr_str = "".join(output_color_fr)
    return output_color_fr_str

color_fr_list = [color_fr(re_color_fr,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#COLOR_EN
re_color_en = r".*(Black|White|Yellow|Blue|Red|Green|Purple|Pink|Orange|Grey|Brown|Bordeaux|Coral|Turquoise|Khaki|Beige|Gold|Silver|Copper|Multicoloured|BLACK|WHITE|YELLOW|BLUE|RED|GREEN|PURPLE|PINK|ORANGE|GREY|BROWN|BORDEAUX|CORAL|TURQUOISE|KHAKI|BEIGE|GOLD|SILVER|COPPER|MULTICOLOURED).*"
def color_en(re_color_en,n):
    global output_color_en_str
    output_color_en = re.split(re_color_en,libelle_list[n])
    if len(output_color_en) >= 0:
        del output_color_en[0]
    if len(output_color_en) >= 1:
        del output_color_en[1]
    output_color_en_str = "".join(output_color_en)
    return output_color_en_str

color_en_list = [color_en(re_color_en,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#COLOR_ORIGINE
re_color_origin = r".*(Argent|Chrome|Fushia).*"
def color_origin(re_color_origin,n):
    global output_color_origin_str
    output_color_origin = re.split(re_color_origin,libelle_list[n])
    if len(output_color_origin) >= 0:
        del output_color_origin[0]
    if len(output_color_origin) >= 1:
        del output_color_origin[1]
    output_color_origin_str = "".join(output_color_origin)
    return output_color_origin_str

color_origin_list = [color_origin(re_color_origin,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#COLOR_ID
re_color_id = r".*(Noir|Blanc|Jaune|Bleu|Rouge|Vert|Violet|Rose|Orange|Gris|Marron|Bordeaux|Corail|Turquoise|Kaki|Beige|Doré|Argent|Cuivre|Multicolore|Black|White|Yellow|Blue|Red|Green|Purple|Pink|Orange|Grey|Brown|Bordeaux|Coral|Turquoise|Khaki|Beige|Gold|Silver|Copper|Multicoloured|NOIR|BLANC|JAUNE|BLEU|ROUGE|VERT|VIOLET|ROSE|ORANGE|GRIS|MARRON|BORDEAUX|CORAIL|TURQUOISE|KAKI|BEIGE|DORÉ|ARGENT|CUIVRE|MULTICOLORE|BLACK|WHITE|YELLOW|BLUE|RED|GREEN|PURPLE|PINK|ORANGE|GREY|BROWN|BORDEAUX|CORAL|TURQUOISE|KHAKI|BEIGE|GOLD|SILVER|COPPER|MULTICOLOURED).*"
def color_id(re_color_id,n):
    global output_color_id_str
    global output_color_id
    output_color_id = re.split(re_color_id,libelle_list[n])
    if len(output_color_id) >= 0:
        del output_color_id[0]
    if len(output_color_id) >= 1:
        del output_color_id[1]
    if output_color_id == ['Noir'] or output_color_id == ['Black'] or output_color_id == ['NOIR'] or output_color_id == ['BLACK']:
        output_color_id = ['1']
    if output_color_id == ['Blanc'] or output_color_id == ['White'] or output_color_id == ['BLANC'] or output_color_id == ['WHITE']:
        output_color_id = ['2']
    if output_color_id == ['Jaune'] or output_color_id == ['Yellow'] or output_color_id == ['JAUNE'] or output_color_id == ['YELLOW']:
        output_color_id = ['3']
    if output_color_id == ['Bleu'] or output_color_id == ['Blue'] or output_color_id == ['BLEU'] or output_color_id == ['BLUE']:
        output_color_id = ['4']
    if output_color_id == ['Rouge'] or output_color_id == ['Red'] or output_color_id == ['ROUGE'] or output_color_id == ['RED']:
        output_color_id = ['5']
    if output_color_id == ['Vert'] or output_color_id == ['Green'] or output_color_id == ['VERT'] or output_color_id == ['GREEN']:
        output_color_id = ['6']
    if output_color_id == ['Violet'] or output_color_id == ['Purple'] or output_color_id == ['VIOLET'] or output_color_id == ['PURPLE']:
        output_color_id = ['7']
    if output_color_id == ['Rose'] or output_color_id == ['Pink'] or output_color_id == ['ROSE'] or output_color_id == ['PINK']:
        output_color_id = ['8']
    if output_color_id == ['Orange'] or output_color_id == ['ORANGE']:
        output_color_id = ['9']
    if output_color_id == ['Gris'] or output_color_id == ['Grey'] or output_color_id == ['GRIS'] or output_color_id == ['GREY']:
        output_color_id = ['10']
    if output_color_id == ['Marron'] or output_color_id == ['Brown'] or output_color_id == ['MARRON'] or output_color_id == ['BROWN']:
        output_color_id = ['11']
    if output_color_id == ['Bordeaux'] or output_color_id == ['BORDEAUX']:
        output_color_id = ['12']
    if output_color_id == ['Corail'] or output_color_id == ['Coral'] or output_color_id == ['CORAIL'] or output_color_id == ['CORAL']:
        output_color_id = ['13']
    if output_color_id == ['Turquoise'] or output_color_id == ['TURQUOISE']:
        output_color_id = ['14']
    if output_color_id == ['Kaki'] or output_color_id == ['Khaki'] or output_color_id == ['KAKI'] or output_color_id == ['KHAKI']:
        output_color_id = ['15']
    if output_color_id == ['Beige'] or output_color_id == ['BEIGE']:
        output_color_id = ['16']
    if output_color_id == ['Doré'] or output_color_id == ['Gold'] or output_color_id == ['DORE'] or output_color_id == ['GOLD']:
        output_color_id = ['17']
    if output_color_id == ['Argent'] or output_color_id == ['Silver'] or output_color_id == ['ARGENT'] or output_color_id == ['SILVER']:
        output_color_id = ['18']
    if output_color_id == ['Cuivre'] or output_color_id == ['Copper'] or output_color_id == ['CUIVRE'] or output_color_id == ['COPPER']:
        output_color_id = ['19']
    if output_color_id == ['Multicolore'] or output_color_id == ['Multicoloured']or output_color_id == ['MULTICOLORE'] or output_color_id == ['MULTICOLOURED']:
        output_color_id = ['99']
    output_color_id_str = "".join(output_color_id)
    return output_color_id_str

color_id_list = [color_id(re_color_id,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#TPI
regex1 = r".* ([0-9]+ Tpi+).*" #Sert à trouver la pression en Tpi
def tpi(regex1,n):
    global output_rex1_str
    output_rex1 = re.split(regex1,libelle_list[n])
    if len(output_rex1) >= 0:
        del output_rex1[0]
    if len(output_rex1) >= 1:
        del output_rex1[1]
    output_rex1_str = "".join(output_rex1)
    return  output_rex1_str

tpi_list = [tpi(regex1,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#TEETH_NB
re_teeth_nb = r"([0-9\/]{2}[D])|([0-9\/]{2} dents)"
def teeth_nb(re_teeth_nb,n):
    global output_teeth_nb_str
    global output_teeth_nb
    if code_art_libelle_list[0][n] == 'M_PLATEAUX' or code_art_libelle_list[0][n] == 'M_PIGNONS':
        output_teeth_nb = re.split(re_teeth_nb,libelle_list[n])
        if len(output_teeth_nb) >= 0:
            del output_teeth_nb[0]
        if len(output_teeth_nb) >= 1:
            if output_teeth_nb[1] == None:
                if len(output_teeth_nb) >= 1:
                    del output_teeth_nb[1]
            else:
                if len(output_teeth_nb) >= 0:
                    del output_teeth_nb[0]
        if len(output_teeth_nb) >= 1:
            del output_teeth_nb[1]
    else:
        output_teeth_nb = ""
    output_teeth_nb_str = "".join(output_teeth_nb)
    return output_teeth_nb_str

teeth_nb_list = [teeth_nb(re_teeth_nb,n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#PRODUCT_NAME_DECLI
def product_name_decli(n):
    output_prod_name_decli = modele(re_model1,re_model2,re_mod_100,re_mod_1,re_mod_2,re_mod_35,n) + ' '+length(regex_len,n) + ' '+color_fr(re_color_fr, n) + ' '+color_en(re_color_en, n)
    return output_prod_name_decli

product_name_decli_list = [product_name_decli(n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#

#DEL_ELT
def del_tpi(n):
    global output_del_tpi
    output_del_tpi = libelle_list[n].replace(tpi(regex1,n),'')
    return output_del_tpi

del_tpi_list = [del_tpi(n) for n in range(1840)]

#-----------------------------------------------------------------------------#
#DEL_DIAMETRE
def del_diametre(n):
    global output_del_diametre
    output_del_diametre = del_tpi_list[n].replace(diametre(regex2,n),'')
    return output_del_diametre

del_diametre_list = [del_diametre(n) for n in range(1840)]

#-----------------------------------------------------------------------------#
test_list = ["0" for i in range(1840)]
#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#

# Création du tableau CSV final

C = {"Libelle" : libelle_list,
"AUTONOMY" : autonomy_list,
"BAR" : bar_list,
"BIKE_NB" : vide_list,
"CAPACITY" : capacity_list,
"COMPATIBILITY_REF" : compatibility_ref_list,
"DIAM_AXE" : diametre_list,
"DIAMETER" : diametre_list,
"DIM_TEMP" : dim_temp_list,
"EAN13" : ean13_list,
"ENTRAXE" : entraxe_list,
"FIXATION_INCLUDED" : non_list,
"FIXATION_ON" : vide_list,
"FUNCTION_NB" : un_list,
"HEIGHT" : height_list,
"LENGTH" : len_list,
"LUMEN" : lumen_list,
"MODELE" : modele_list,
"PIECE_NB" : un_list,
"PILE_INCLUDED" : pile_inclu_list,
"PILE_NB" : vide_list,
"PILE_TYPE" : vide_list,
"PRODUCT_NAME_DECLI" : product_name_decli_list,
"PRODUCT_NAME" : modele_list,
"REGLABLE" : reglable_list,
"RIM_TYPE" : rim_type_list,
"RIM_WIDTH" : rim_width_list,
"SIZE_GLOBAL" : size_global_list,
"SIZE_ID" : zero_list,
"SIZE_LABEL" : size_label_list,
"SPEED_NB" : speednb_list,
"TIGE_SELLE" : tige_list,
"TORX" : torx_list,
"VIS_TYPE" : vide_list,
"VISCOSITY" : viscosity_list,
"VOLT" : volt_list,
"WATT" : watt_list,
"WEIGHT" : weight_list,
"WEIGHT_MAX" : vide_list,
"WHEEL_ETRTO" : wheel_etrto_list,
"WHEEL_FR" : wheel_fr_list,
"WHEEL_INCH" : wheel_inch_list,
"WHEEL_WIDTH" : wheel_width_list,
"WIDTH" : diametre_list,
"COLOR_FR" : color_fr_list,
"COLOR_EN" : color_en_list,
"COLOR_ORIGINE" : color_origin_list,
"COLOR_ID" : color_id_list,
"TPI" : tpi_list,
"TEETH_NB" : teeth_nb_list,
}
donnes = DataFrame(C, columns = ["Libelle", "AUTONOMY", "BAR", "BIKE_NB","CAPACITY","COMPATIBILITY_REF","DIAM_AXE","DIAMETER","DIM_TEMP","EAN13","ENTRAXE","FIXATION_INCLUDED","FIXATION_ON","FUNCTION_NB","HEIGHT","LENGTH","LUMEN","MODELE","PIECE_NB","PILE_INCLUDED","PILE_NB","PILE_TYPE","PRODUCT_NAME_DECLI","PRODUCT_NAME","REGLABLE","RIM_TYPE","RIM_WIDTH","SIZE_GLOBAL","SIZE_ID","SIZE_LABEL","SPEED_NB","TIGE_SELLE","TORX","VIS_TYPE","VISCOSITY","VOLT","WATT","WEIGHT","WEIGHT_MAX","WHEEL_ETRTO","WHEEL_FR","WHEEL_INCH","WHEEL_WIDTH","WIDTH","COLOR_FR","COLOR_EN","COLOR_ORIGINE","COLOR_ID","TPI","TEETH_NB"])
export_csv = donnes.to_csv("Table_finale_stage.csv", index=None,header=True,encoding='utf-8', sep=';',)
print(donnes)

#-------------------------------------------------------------------------------------------------#