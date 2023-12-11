import tkinter 
from tkinter import *
root = Tk()
root.title("Grocery Shopping Bill")
root.geometry("1400x800")        
#=====================================
bg_color = "pink"
fg_color = "white"
label_color = "white"
        
#function to get total price
def Calculation():
    can = int(cannedfood.get())
    bev = int(beverages.get())
    bab = int(babykits.get())
    fro = int(frozenfood.get())
    cer = int(cereals.get())
    gra = int(grains.get())
    fru = int(fruits.get())
    con = int(condiments.get())
    cook = int(cookingoil.get())
    toil = int(toiletries.get())
    pet = int(pet_items.get())
    spo = int(sport_kits.get())
        
    Total_Product = (can + bev + bab + fro + cer + gra + fru + con + cook + toil + pet + spo)
    Label(text=f"{Total_Product}", font="arial 15 bold").place(x=100,y=300)
    # Total_Vat = int(Total_Product * 0.05)
    # Label(text=f"{Total_Vat}", font="arial 15 bold").place(x=270,y=300)
#total price
    pri1 = int(price1_Entry.get())
    pri2 = int(price2_Entry.get())
    pri3 = int(price3_Entry.get())
    pri4 = int(price4_Entry.get())
    pri5 = int(price5_Entry.get())
    pri6 = int(price6_Entry.get())
    pri7 = int(price7_Entry.get())
    pri8 = int(price8_Entry.get())
    pri9 = int(price9_Entry.get())
    pri10 = int(price10_Entry.get())
    pri11 = int(price11_Entry.get())
    pri12 = int(price12_Entry.get())

#total quantity    
    quan1 = int(quantity1_Entry.get())
    quan2 = int(quantity2_Entry.get())
    quan3 = int(quantity3_Entry.get())
    quan4 = int(quantity4_Entry.get())
    quan5 = int(quantity5_Entry.get())
    quan6 = int(quantity6_Entry.get())
    quan7 = int(quantity7_Entry.get())
    quan8 = int(quantity8_Entry.get())
    quan9 = int(quantity9_Entry.get())
    quan10 = int(quantity10_Entry.get())
    quan11 = int(quantity11_Entry.get())
    quan12 = int(quantity12_Entry.get())

#total amount
    total_amount1_value = pri1 + quan1
    Label(text=f"{total_amount1_value}", font="arial 15 bold").place(x=40,y=90)
    total_amount2_value = pri2 + quan2
    Label(text=f"{total_amount2_value}", font="arial 15 bold").place(x=40,y=130)
    total_amount3_value = pri3 + quan3
    Label(text=f"{total_amount3_value}", font="arial 15 bold").place(x=40,y=170)
    total_amount4_value = pri4 + quan4
    Label(text=f"{total_amount4_value}", font="arial 15 bold").place(x=40,y=210)
    total_amount5_value = pri5 + quan5
    Label(text=f"{total_amount5_value}", font="arial 15 bold").place(x=40,y=250)
    total_amount6_value = pri6 + quan6
    Label(text=f"{total_amount6_value}", font="arial 15 bold").place(x=40,y=290)
    total_amount7_value = pri7 + quan7
    Label(text=f"{total_amount7_value}", font="arial 15 bold").place(x=40,y=330)
    total_amount8_value = pri8 + quan8
    Label(text=f"{total_amount8_value}", font="arial 15 bold").place(x=40,y=370)
    total_amount9_value = pri9 + quan9
    Label(text=f"{total_amount9_value}", font="arial 15 bold").place(x=40,y=410)
    total_amount10_value = pri10 + quan10
    Label(text=f"{total_amount10_value}", font="arial 15 bold").place(x=40,y=450)
    total_amount11_value = pri11 + quan11
    Label(text=f"{total_amount11_value}", font="arial 15 bold").place(x=40,y=490)
    total_amount12_value = pri12 + quan12
    Label(text=f"{total_amount12_value}", font="arial 15 bold").place(x=40,y=530)
    

#Total Vat
    vat1_value = 0.0075 * total_amount1_value
    Label(text=f"{vat1_value}", font="arial 15 bold").place(x=40,y=90)
    vat2_value = 0.0075 * total_amount2_value
    Label(text=f"{vat2_value}", font="arial 15 bold").place(x=40,y=130)
    vat3_value = 0.0075 * total_amount3_value
    Label(text=f"{vat3_value}", font="arial 15 bold").place(x=40,y=170)
    vat4_value = 0.0075 * total_amount4_value
    Label(text=f"{vat4_value}", font="arial 15 bold").place(x=40,y=210)
    vat5_value = 0.0075 * total_amount5_value
    Label(text=f"{vat5_value}", font="arial 15 bold").place(x=40,y=250)
    vat6_value = 0.0075 * total_amount6_value
    Label(text=f"{vat6_value}", font="arial 15 bold").place(x=40,y=290)
    vat7_value = 0.0075 * total_amount7_value
    Label(text=f"{vat7_value}", font="arial 15 bold").place(x=40,y=330)
    vat8_value = 0.0075 * total_amount8_value
    Label(text=f"{vat8_value}", font="arial 15 bold").place(x=40,y=370)
    vat9_value = 0.0075 * total_amount9_value
    Label(text=f"{vat9_value}", font="arial 15 bold").place(x=40,y=410)
    vat10_value = 0.0075 * total_amount10_value
    Label(text=f"{vat10_value}", font="arial 15 bold").place(x=40,y=450)
    vat11_value = 0.0075 * total_amount11_value
    Label(text=f"{vat11_value}", font="arial 15 bold").place(x=40,y=490)
    vat12_value = 0.0075 * total_amount12_value
    Label(text=f"{vat12_value}", font="arial 15 bold").place(x=40,y=530)
    
#total grocery amount

    
    
    
 
    
def clear(self):
    self.txt.delete(0,END)

product = Label(root,text="Product: ", font="arial 10")
quantity = Label(root,text="Quantity: ", font="arial 10")
price = Label(root,text="Price: ", font="arial 10")
vat = Label(root,text="VAT: ", font="arial 10")
total_amount = Label(root,text="Total Amount: ", font="arial 10")
print = Label(text="===============================================================================")


cannedfood = Label(root,text="Canned Food: ", font="arial 10").place(x=20,y=70)
beverages = Label(root,text="Beverages: ", font="arial 10").place(x=20,y=105)
babykits = Label(root,text="Baby Kits: ", font="arial 10").place(x=20,y=140)
frozenfood = Label(root,text="Frozen Food: ", font="arial 10").place(x=20,y=175)
cereals = Label(root,text="Cereals: ", font="arial 10").place(x=20,y=210)
grains = Label(root,text="Grains: ", font="arial 10").place(x=20,y=245)
fruits = Label(root,text="Fruits: ", font="arial 10").place(x=20,y=280)
condiments = Label(root,text="Condiments: ", font="arial 10").place(x=20,y=315)
cookingoil = Label(root,text="Cooking Oil: ", font="arial 10").place(x=20,y=350)
toiletries = Label(root,text="Toiletries: ", font="arial 10").place(x=20,y=385)
pet_items =  Label(root,text="Pet Items: ", font="arial 10").place(x=20,y=420)
sport_kits = Label(root,text="Sport Kits: ", font="arial 10").place(x=20,y=455)


total_product = Label(root, text="Total Product: ", font="arial 10")
total_quantity = Label(root, text="Total Quantity: ", font="arial 10")
total_vat = Label(root, text="Total VAT: ", font="arial 10")
total_grocery_amount = Label(root, text="Total Grocery Amount: ", font="arial 10")

product.place(x=40,y=20)
quantity.place(x=150,y=20)
price.place(x=260,y=20)
vat.place(x=370,y=20)
total_amount.place(x=480,y=20)
print.place(x=10,y=40)

total_product.place(x=20,y=500)
total_quantity.place(x=150,y=500)
total_vat.place(x=500,y=500)
total_grocery_amount.place(x=300,y=500)

product_value = StringVar()
quantity_value = StringVar()
price_value = StringVar()
vat1_value = StringVar()
total_amount1_value = StringVar()


product_Entry = Entry(root,textvariable=product_value, font="arial 15",width=15)
quantity1_Entry = Entry(root,textvariable=quantity_value, font="arial 15",width=15)
price1_Entry = Entry(root,textvariable=price_value, font="arial 15",width=15)
vat1_Entry = Entry(root,textvariable=vat1_value, font="arial 15",width=15)
total_amount1_Entry = Entry(root,textvariable=total_amount1_value, font="arial 15",width=15)


quantity1_Entry.place(x=150,y=65)
price1_Entry.place(x=250,y=65)
vat1_Entry.place(x=350,y=65)
total_amount1_Entry.place(x=450,y=65)


product_p_value = StringVar()
quantity_q_value = StringVar()
price_p_value = StringVar()
vat2_value = StringVar()
total_amount2_value = StringVar()


product_Entry = Entry(root,textvariable=product_p_value, font="arial 15",width=15)
quantity2_Entry = Entry(root,textvariable=quantity_q_value, font="arial 15",width=15)
price2_Entry = Entry(root,textvariable=price_p_value, font="arial 15",width=15)
vat2_Entry = Entry(root,textvariable=vat2_value, font="arial 15",width=15)
total_amount2_Entry = Entry(root,textvariable=total_amount2_value, font="arial 15",width=15)


quantity2_Entry.place(x=150,y=102)
price2_Entry.place(x=250,y=102)
vat2_Entry.place(x=350,y=102)
total_amount2_Entry.place(x=450,y=102)



product_p_value = StringVar()
quantity_u_value = StringVar()
price_r_value = StringVar()
vat3_value = StringVar()
total_amount3_value = StringVar()


product_Entry = Entry(root,textvariable=product_p_value, font="arial 15",width=15)
quantity3_Entry = Entry(root,textvariable=quantity_u_value, font="arial 15",width=15)
price3_Entry = Entry(root,textvariable=price_r_value, font="arial 15",width=15)
vat3_Entry = Entry(root,textvariable=vat3_value, font="arial 15",width=15)
total_amount3_Entry = Entry(root,textvariable=total_amount3_value, font="arial 15",width=15)


quantity3_Entry.place(x=150,y=138)
price3_Entry.place(x=250,y=138)
vat3_Entry.place(x=350,y=138)
total_amount3_Entry.place(x=450,y=138)


product_p_value = StringVar()
quantity_t_value = StringVar()
price_i_value = StringVar()
vat4_value = StringVar()
total_amount4_value = StringVar()



product_Entry = Entry(root,textvariable=product_p_value, font="arial 15",width=15)
quantity4_Entry = Entry(root,textvariable=quantity_t_value, font="arial 15",width=15)
price4_Entry = Entry(root,textvariable=price_i_value, font="arial 15",width=15)
vat4_Entry = Entry(root,textvariable=vat4_value, font="arial 15",width=15)
total_amount4_Entry = Entry(root,textvariable=total_amount4_value, font="arial 15",width=15)



quantity4_Entry.place(x=150,y=172)
price4_Entry.place(x=250,y=172)
vat4_Entry.place(x=350,y=172)
total_amount4_Entry.place(x=450,y=172)


product_p_value = StringVar()
quantity_y_value = StringVar()
price_j_value = StringVar()
vat5_value = StringVar()
total_amount5_value = StringVar()



product_Entry = Entry(root,textvariable=product_p_value, font="arial 15",width=15)
quantity5_Entry = Entry(root,textvariable=quantity_y_value, font="arial 15",width=15)
price5_Entry = Entry(root,textvariable=price_j_value, font="arial 15",width=15)
vat5_Entry = Entry(root,textvariable=vat5_value, font="arial 15",width=15)
total_amount5_Entry = Entry(root,textvariable=total_amount5_value, font="arial 15",width=15)



quantity5_Entry.place(x=150,y=205)
price5_Entry.place(x=250,y=205)
vat5_Entry.place(x=350,y=205)
total_amount5_Entry.place(x=450,y=205)


product_p_value = StringVar()
quantity_r_value = StringVar()
price_c_value = StringVar()
vat6_value = StringVar()
total_amount6_value = StringVar()



product_Entry = Entry(root,textvariable=product_p_value, font="arial 15",width=15)
quantity6_Entry = Entry(root,textvariable=quantity_r_value, font="arial 15",width=15)
price6_Entry = Entry(root,textvariable=price_c_value, font="arial 15",width=15)
vat6_Entry = Entry(root,textvariable=vat6_value, font="arial 15",width=15)
total_amount6_Entry = Entry(root,textvariable=total_amount6_value, font="arial 15",width=15)



quantity6_Entry.place(x=150,y=239)
price6_Entry.place(x=250,y=239)
vat6_Entry.place(x=350,y=239)
total_amount6_Entry.place(x=450,y=239)


product_p_value = StringVar()
quantity_t_value = StringVar()
price_g_value = StringVar()
vat7_value = StringVar()
total_amount7_value = StringVar()


product_Entry = Entry(root,textvariable=product_p_value, font="arial 15",width=15)
quantity7_Entry = Entry(root,textvariable=quantity_t_value, font="arial 15",width=15)
price7_Entry = Entry(root,textvariable=price_g_value, font="arial 15",width=15)
vat7_Entry = Entry(root,textvariable=vat7_value, font="arial 15",width=15)
total_amount7_Entry = Entry(root,textvariable=total_amount7_value, font="arial 15",width=15)


quantity7_Entry.place(x=150,y=273)
price7_Entry.place(x=250,y=273)
vat7_Entry.place(x=350,y=273)
total_amount7_Entry.place(x=450,y=273)



product_p_value = StringVar()
quantity_o_value = StringVar()
price_i_value = StringVar()
vat8_value = StringVar()
total_amount8_value = StringVar()


product_Entry = Entry(root,textvariable=product_p_value, font="arial 15",width=15)
quantity8_Entry = Entry(root,textvariable=quantity_o_value, font="arial 15",width=15)
price8_Entry = Entry(root,textvariable=price_i_value, font="arial 15",width=15)
vat8_Entry = Entry(root,textvariable=vat8_value, font="arial 15",width=15)
total_amount8_Entry = Entry(root,textvariable=total_amount8_value, font="arial 15",width=15)



quantity8_Entry.place(x=150,y=308)
price8_Entry.place(x=250,y=308)
vat8_Entry.place(x=350,y=308)
total_amount8_Entry.place(x=450,y=308)

product_p_value = StringVar()
quantity_h_value = StringVar()
price_h_value = StringVar()
vat9_value = StringVar()
total_amount9_value = StringVar()



product_Entry = Entry(root,textvariable=product_p_value, font="arial 15",width=15)
quantity9_Entry = Entry(root,textvariable=quantity_h_value, font="arial 15",width=15)
price9_Entry = Entry(root,textvariable=price_h_value, font="arial 15",width=15)
vat9_Entry = Entry(root,textvariable=vat9_value, font="arial 15",width=15)
total_amount9_Entry = Entry(root,textvariable=total_amount9_value, font="arial 15",width=15)


quantity9_Entry.place(x=150,y=343)
price9_Entry.place(x=250,y=343)
total_amount9_Entry.place(x=450,y=343)
vat9_Entry.place(x=350,y=343)


product_p_value = StringVar()
quantity_g_value = StringVar()
price_g_value = StringVar()
total_amount10_value = StringVar()
vat10_value = StringVar()

product_Entry = Entry(root,textvariable=product_p_value, font="arial 15",width=15)
quantity10_Entry = Entry(root,textvariable=quantity_g_value, font="arial 15",width=15)
price10_Entry = Entry(root,textvariable=price_g_value, font="arial 15",width=15)
vat10_Entry = Entry(root,textvariable=vat10_value, font="arial 15",width=15)
total_amount10_Entry = Entry(root,textvariable=total_amount10_value, font="arial 15",width=15)


quantity10_Entry.place(x=150,y=378)
price10_Entry.place(x=250,y=378)
vat10_Entry.place(x=350,y=378)
total_amount10_Entry.place(x=450,y=378)


product_p_value = StringVar()
quantity_j_value = StringVar()
price_j_value = StringVar()
total_amount11_value = StringVar()
vat11_value = StringVar()


product_Entry = Entry(root,textvariable=product_p_value, font="arial 15",width=15)
quantity11_Entry = Entry(root,textvariable=quantity_j_value, font="arial 15",width=15)
price11_Entry = Entry(root,textvariable=price_j_value, font="arial 15",width=15)
vat11_Entry = Entry(root,textvariable=vat11_value, font="arial 15",width=15)
total_amount11_Entry = Entry(root,textvariable=total_amount11_value, font="arial 15",width=15)


quantity11_Entry.place(x=150,y=415)
price11_Entry.place(x=250,y=415)
vat11_Entry.place(x=350,y=415)
total_amount11_Entry.place(x=450,y=415)


product_p_value = StringVar()
quantity_b_value = StringVar()
price_b_value = StringVar()
total_amount12_value = StringVar()
vat12_value = StringVar()

product_Entry = Entry(root,textvariable=product_p_value, font="arial 15",width=15)
quantity12_Entry = Entry(root,textvariable=quantity_b_value, font="arial 15",width=15)
price12_Entry = Entry(root,textvariable=price_b_value, font="arial 15",width=15)
vat12_Entry = Entry(root,textvariable=vat12_value, font="arial 15",width=15)
total_amount12_Entry = Entry(root,textvariable=total_amount12_value, font="arial 15",width=15)


quantity12_Entry.place(x=150,y=452)
price12_Entry.place(x=250,y=452)
vat12_Entry.place(x=350,y=452)
total_amount12_Entry.place(x=450,y=452)


Button(text="Calculate", font="arial 15",bg="white", bd=15).place(x=25,y=600)
Button(text="Exit", font="arial 15",bg="blue", width=8, bd=15, command=lambda:exit()).place(x=200,y=600)

root.mainloop()


