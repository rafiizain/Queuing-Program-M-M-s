import math
from tkinter import *

class MyWindow:
    def __init__(self, win):
        self.lbl00 = Label(win, text="Program M/M/1 dan M/M/s ")
        self.lbl00.place(x=50, y=25)
        self.lbl01 = Label(win, text="Kelompok 5: ")
        self.lbl01.place(x=50, y=50)
        self.lbl02 = Label(win, text="Farhan Rafiqi (1806195242)")
        self.lbl02.place(x=50, y=75)
        self.lbl03 = Label(win, text="George Simon Tongam (1806147905)")
        self.lbl03.place(x=50, y=100)
        self.lbl04 = Label(win, text="Hazel Raditya Mizumareru (1806194851)")
        self.lbl04.place(x=50, y=125)
        self.lbl05 = Label(win, text="Muhammad Rafii Zain (1806195160)")
        self.lbl05.place(x=50, y=150)
        self.lbl06 = Label(win, text="Ruben Namata (1806195091)")
        self.lbl06.place(x=50, y=175)
        self.lbl2 = Label(win, text="mean arrival rate (Lambda): ")
        self.lbl2.place(x=50, y=250)
        self.Lambda=Entry(bd=3)
        self.Lambda.place(x=200, y=250)
        self.lbl3 = Label(win, text="mean service rate (Mu): ")
        self.lbl3.place(x=50, y=300)
        self.Mu=Entry()
        self.Mu.place(x=200, y=300)
        self.lbl4 = Label(win, text="Number of Servers (s): ")
        self.lbl4.place(x=50, y=350)
        self.s=Entry()
        self.s.place(x=200, y=350)
        self.b1=Button(win, text="Calculate", command=self.Result)
        self.b1.place(x=150, y=400)
        self.lbl5 = Label(win, text="Queuing Intensity (Rho): ")
        self.lbl5.place(x=50, y=450)
        self.Rho=Entry()
        self.Rho.place(x=200, y=450)
        self.lbl6 = Label(win, text="Length in Queue (Lq): ")
        self.lbl6.place(x=50, y=500)
        self.Lq=Entry()
        self.Lq.place(x=200, y=500)
        self.lbl7 = Label(win, text="Length in System (L): ")
        self.lbl7.place(x=50, y=550)
        self.L=Entry()
        self.L.place(x=200, y=550)
        self.lbl8 = Label(win, text="Waiting in Queue (Wq): ")
        self.lbl8.place(x=50, y=600)
        self.Wq=Entry()
        self.Wq.place(x=200, y=600)
        self.lbl9 = Label(win, text="Waiting in System (W): ")
        self.lbl9.place(x=50, y=650)
        self.W=Entry()
        self.W.place(x=200, y=650)
        self.lbl9 = Label(win, text="Probability of Idle Server: ")
        self.lbl9.place(x=50, y=700)
        self.p0=Entry()
        self.p0.place(x=200, y=700)
        
    def Result(self):
        self.Rho.delete(0, 'end')
        self.Lq.delete(0, 'end')
        self.L.delete(0, 'end')
        self.Wq.delete(0, 'end')
        self.W.delete(0, 'end')
        self.p0.delete(0, 'end')
            
        Lambda=int(self.Lambda.get())
        Mu=int(self.Mu.get())
        s=int(self.s.get())
            
        if s == 1:            
            Rho = Lambda / Mu
            Rho_Persen = Rho * 100 
            L = Rho / (1 - Rho)
            Lq = (Rho**2) / (1- Rho)
            Es = 1 / Mu

            W = Es / (1 - Rho)
            Wq = (Rho * Es) / (1 - Rho)
            p0 = 1 - Rho
            
            self.Rho.insert(END, str(Rho))
            self.Lq.insert(END, str(Lq))
            self.L.insert(END, str(L))
            self.Wq.insert(END, str(Wq))
            self.W.insert(END, str(W))
            self.p0.insert(END, str(p0))
            print("Queuing Intensity: ", Rho)
            print("Queuing Utilization: ", Rho_Persen,"%")
            print("Queue Length in Queue: ", Lq)
            print("Queue Length in System: ", L)
            print("Delay in Queue", Wq)
            print("Delay in System", W)
            print("Probability of idle server:", p0)
    
        elif s == 0:
            print("Mohon Input s selain 0")
            
        else:
            Rho = Lambda / (s * Mu)
            Rho_Persen = Rho * 100 
            
            n=0
            kiri=0
            
            while n <= s-1:
                ini = ((Lambda / Mu)**n) / (math.factorial(int(n)))
                kiri += ini
                n += 1
                
            tengah = ((Lambda / Mu)**s) / (math.factorial(int(s)))
            kanan = 1 / (1 - (Rho))
            
            p0 = 1 / (kiri + tengah * kanan)
            
            Lq = p0 * (((Lambda / Mu)**s) / math.factorial(int(s))) * ((Rho) / ((1 - Rho)**2))
            L = Lq + (Lambda / Mu)
            Es = 1 / Mu
            Wq = Lq / Lambda
            W = Wq + 1 / Mu
            
            self.Rho.insert(END, str(Rho))
            self.Lq.insert(END, str(Lq))
            self.L.insert(END, str(L))
            self.Wq.insert(END, str(Wq))
            self.W.insert(END, str(W))
            self.p0.insert(END, str(p0))
            print("Queuing Intensity: ", Rho)
            print("Queuing Utilization: ", Rho_Persen,"%")
            print("Queue Length in Queue: ", Lq)
            print("Queue Length in System: ", L)
            print("Delay in Queue", Wq)
            print("Delay in System", W)
            print("Probability of idle server:", p0)

window=Tk()
mywin=MyWindow(window)
window.title('Program M/M/1 dan M/M/s')
window.geometry("400x800+10+10")
window.mainloop()    