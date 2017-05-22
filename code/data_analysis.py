class data_analysis_cells:
    def __init__(self, ΔA = 20, ΔB = 20, result_one_trial = None):
        self.list_choice=['A', 'B']

        self.ΔA = ΔA
        self.ΔB = ΔB
        self.result_one_trial = result_one_trial
        self.result = {}  # contains all the average of each firing depending on (#A, #B, choice)
        for i in range(self.ΔA +1):
            for j in range(self.ΔB +1):
                for choice_i in self.list_choice:
                    self.result[(i,j,choice_i)]= []

        self.ovb_rate_low, self.ovb_rate_medium, self.ovb_rate_high = [], [], [] #for figure 4A
        self.mean_A_chosen_cj, self.mean_B_chosen_cj = [], []
        self.mean_low_cv, self.mean_medium_cv, self.mean_high_cv = [], [], []
        self.ov_choiceA, self.cjb_choiceA, self.cv_choiceA = [], [], []
        self.ov_choiceB, self.cjb_choiceB, self.cv_choiceB = [], [], []
        self.choice_A, self.choice_B = {},{}
        self.firing_D = [] # for figure 4D
        self.firing_H_A, self.firing_H_B = [], [] # for figure 4H
        self.X_A, self.X_B, self.Y_A, self.Y_B = [], [], [], [] # for firgure 4L
        self.tuning_ov, self.tuning_cjb, self.tuning_cv = [], [], [] # for tuning curve
        self.offer_A, self.firing_cja, self.firing_cjb = [], [], []
        self.colour = ['red', 'orange', 'yellow', 'green', 'green', 'green', 'blue', '']

        """ average of firing rate of each cell firing depending on (#A, #B, choice) """
        for t in range(4003): ##verifier le 4003
            for i in range(self.ΔA +1):
                for j in range(self.ΔB+1):
                    for choice_i in self.list_choice:
                        for t in range(4003):
                            mean_ovb, mean_cja, mean_cjb, mean_ns, mean_cv = 0, 0, 0, 0, 0
                            number_trial = 0
                            for l in range(len(self.result_one_trial[(i,j,choice_i)])):
                                mean_ovb += self.result_one_trial[(i,j,choice_i)][l][0][t]
                                mean_cja += self.result_one_trial[(i,j,choice_i)][l][1][t]
                                mean_cjb += self.result_one_trial[(i,j,choice_i)][l][2][t]
                                mean_ns += self.result_one_trial[(i,j,choice_i)][l][3][t]
                                mean_cv += self.result_one_trial[(i,j,choice_i)][l][4][t]
                                number_trial += 1
                            self.result[(i,j,choice_i)].append(mean_ovb / number_trial)
                            self.result[(i, j, choice_i)].append(mean_cja / number_trial)
                            self.result[(i,j,choice_i)].append(mean_cjb / number_trial)
                            self.result[(i,j,choice_i)].append(mean_ns / number_trial)
                            self.result[(i,j,choice_i)].append(mean_cv / number_trial)

    def average_firing_rate_B_ov(self):
        """average of firing rate of cells dependind on the quantity of juice B : low, medium, high (fig.4)"""
        for k in range(4001):
            mean_ov_low, mean_ov_high, mean_ov_medium = 0, 0, 0
            low, medium, high = 0, 0, 0
            for i in range(0, self.ΔA +1):
                for j in range(0, round(self.ΔB / 3)):
                    for choice_i in self.list_choice:
                        if self.result[(i, j, choice_i)] == []:
                            mean_ov_low += 0
                        else:
                            mean_ov_low += self.result[(i, j, choice_i)][0][0][k]
                            low += 1
                for j in range(round(self.ΔB / 3), round(self.ΔB * 2/3)):
                    for choice_i in self.list_choice:
                        if self.result[(i, j, choice_i)] == []:
                            mean_ov_medium += 0
                        else:
                            mean_ov_medium += self.result[(i, j, choice_i)][0][0][k]
                            medium += 1
                for j in range(round(self.ΔB * 2/3), self.ΔB +1):
                    for choice_i in self.list_choice:
                        if self.result[(i, j, choice_i)] == []:
                            mean_ov_high += 0
                        else:
                            mean_ov_high += self.result[(i, j, choice_i)][0][0][k]
                            high += 1
            self.ovb_rate_low.append(mean_ov_low / low)
            self.ovb_rate_medium.append(mean_ov_medium / medium)
            self.ovb_rate_high.append(mean_ov_high / high)
        return [self.ovb_rate_low, self.ovb_rate_medium, self.ovb_rate_high]


    def average_firing_rate_cj(self):
        '''mean depending on choice (figure 4E, 4I)'''
        for k in range(4002):
            A_chosen_cj, B_chosen_cj = 0, 0
            A_nb, B_nb = 0, 0
            for i in range(self.ΔA + 1):
                for j in range(self.ΔB + 1):
                    for choice_i in self.list_choice:
                        if not len(self.result[(i, j, choice_i)]):
                            A_chosen_cj += 0
                            B_chosen_cj += 0
                        else:
                            if choice_i == 'A':
                                A_chosen_cj += self.result[(i, j, choice_i)][0][1][k]
                                A_nb += 1
                            else:
                                B_chosen_cj += self.result[(i, j, choice_i)][0][1][k]
                                B_nb += 1
            if A_nb == 0: A_nb = 1
            if B_nb == 0: B_nb = 1
            self.mean_A_chosen_cj.append(A_chosen_cj / A_nb)
            self.mean_B_chosen_cj.append(B_chosen_cj / B_nb)
        return [self.mean_A_chosen_cj, self.mean_B_chosen_cj]


    def average_firing_rate_cv(self):
        '''mean depending on choice (figure 4E, 4I)'''
        for k in range(4002):
            chosen_value_low, chosen_value_medium, chosen_value_high = 0, 0, 0
            low_cv, medium_cv, high_cv = 0, 0, 0
            for i in range(self.ΔA + 1):
                for j in range(self.ΔB + 1):
                    for choice_i in self.list_choice:
                        if not len(self.result[(i, j, choice_i)]):
                            chosen_value_low += 0
                            chosen_value_medium += 0
                            chosen_value_high += 0
                        else:
                            if choice_i == 'A':
                                if i < (round(self.ΔA / 3)):
                                    chosen_value_low += self.result[(i, j, choice_i)][0][2][k]
                                    low_cv += 1
                                elif (round(self.ΔA / 3)) < i < (round(self.ΔA * 2 / 3)):
                                    chosen_value_medium += self.result[(i, j, choice_i)][0][2][k]
                                    medium_cv += 1
                                else:
                                    chosen_value_high += self.result[(i, j, choice_i)][0][2][k]
                                    high_cv += 1
                            else:
                                if j < (round(self.ΔB / 3)):
                                    chosen_value_low += self.result[(i, j, choice_i)][0][2][k]
                                    low_cv += 1
                                elif (round(self.ΔB / 3)) < j < (round(self.ΔB * 2 / 3)):
                                    chosen_value_medium += self.result[(i, j, choice_i)][0][2][k]
                                    medium_cv += 1
                                else:
                                    chosen_value_high += self.result[(i, j, choice_i)][0][2][k]
                                    high_cv += 1
            self.mean_low_cv.append(chosen_value_low / low_cv)
            self.mean_medium_cv.append(chosen_value_medium / medium_cv)
            self.mean_high_cv.append(chosen_value_high / high_cv)

        return [self.mean_low_cv, self.mean_medium_cv, self.mean_high_cv]

    def average_firing_time_windows(self):
        """ average of the firing rate of all the cells for certain offers betwwen 1s and 1.5s for OV and CJ cells and 1.5 and 2s for CV cells (check this)"""
        ov_A_choiceA, ov_A_choiceB, ov_B_choiceA, ov_B_choiceB = [], [], [], []
        cjb_A_choiceA, cjb_A_choiceB, cjb_B_choiceA, cjb_B_choiceB = [], [], [], []
        cv_A_choiceA, cv_A_choiceB, cv_B_choiceA, cv_B_choiceB = [], [], [], []

        #Initilisation of mean
        mean_ov_ij, mean_cjb_ij, mean_cv_ij = 0, 0, 0
        mean_ov_ji, mean_cjb_ji, mean_cv_ji = 0, 0, 0
        mean_ov_0B1A, mean_cj_0B1A, mean_cv_0B1A = 0, 0, 0
        mean_ov_1B0A, mean_cj_1B0A, mean_cv_1B0A = 0, 0, 0

        for choice_i in self.list_choice:
            for j in range(self.ΔB, 3, -4):
                if len(self.result[(1, j, choice_i)]) == 0:
                    pass
                else:
                    for k in range(2000, 3001):
                        mean_ov_ij += self.result[(1, j, choice_i)][0][0][k]
                        mean_cjb_ij += self.result[(1, j, choice_i)][0][1][k]
                        mean_cv_ij += self.result[(1, j, choice_i)][0][2][k + 1000]
                if not len(self.result[(j, 1, choice_i)]):
                    pass
                else:
                    for k in range(2000, 3001):
                        mean_ov_ji += self.result[(j, 1, choice_i)][0][0][k]
                        mean_cjb_ji += self.result[(j, 1, choice_i)][0][1][k]
                        mean_cv_ji += self.result[(j, 1, choice_i)][0][2][k + 1000]
                if choice_i == 'A':
                    ov_A_choiceA.append(mean_ov_ij / 1000)
                    ov_B_choiceA.append(mean_ov_ji / 1000)
                    cjb_A_choiceA.append(mean_cjb_ij / 1000)
                    cjb_B_choiceA.append(mean_cjb_ji / 1000)
                    cv_A_choiceA.append(mean_cv_ij / 1000)
                    cv_B_choiceA.append(mean_cv_ji / 1000)
                elif choice_i == 'B':
                    ov_A_choiceB.append(mean_ov_ij / 1000)
                    ov_B_choiceB.append(mean_ov_ji / 1000)
                    cjb_A_choiceB.append(mean_cjb_ij / 1000)
                    cjb_B_choiceB.append(mean_cjb_ji / 1000)
                    cv_A_choiceB.append(mean_cv_ij / 1000)
                    cv_B_choiceB.append(mean_cv_ji / 1000)

            if not len(self.result[(1, 0, choice_i)]):
                mean_ov_0B1A = 0
                mean_cj_0B1A = 0
                mean_cv_0B1A = 0
            else:
                for k in range(2000, 3001):
                    mean_ov_0B1A += self.result[(1, 0, choice_i)][0][0][k]
                    mean_cj_0B1A += self.result[(1, 0, choice_i)][0][1][k]
                    mean_cv_0B1A += self.result[(1, 0, choice_i)][0][2][k + 1000]

            if not len(self.result[(0, 1, choice_i)]):
                mean_ov_1B0A = 0
                mean_cj_1B0A = 0
                mean_cv_1B0A = 0
            else:
                for k in range(2000, 3001):
                    mean_ov_1B0A += self.result[(0, 1, choice_i)][0][0][k]
                    mean_cj_1B0A += self.result[(0, 1, choice_i)][0][1][k]
                    mean_cv_1B0A += self.result[(0, 1, choice_i)][0][2][k + 1000]
            if choice_i == 'A':
                self.ov_choiceA = [mean_ov_0B1A / 1000] + ov_B_choiceA[::-1] + ov_A_choiceA + [mean_ov_1B0A / 1000]
                self.cjb_choiceA = [mean_cj_0B1A / 1000] + cjb_B_choiceA[::-1] + cjb_A_choiceA + [mean_cj_1B0A / 1000]
                self.cv_choiceA = [mean_cv_0B1A / 1000] + cv_B_choiceA[::-1] + cv_A_choiceA + [mean_cv_1B0A / 1000]

            else:
                self.ov_choiceB = [mean_ov_0B1A / 1000] + ov_B_choiceB[::-1] + ov_A_choiceB + [mean_ov_1B0A / 1000]
                self.cjb_choiceB = [mean_cj_0B1A / 1000] + cjb_B_choiceB[::-1] + cjb_A_choiceB + [mean_cj_1B0A / 1000]
                self.cv_choiceB = [mean_cv_0B1A / 1000] + cv_B_choiceB[::-1] + cv_A_choiceB + [mean_cv_1B0A / 1000]
        return self.ov_choiceA, self.cjb_choiceA, self.cv_choiceA, self.ov_choiceB, self.cjb_choiceB, self.cv_choiceB

    def pourcentage_B(self):
        """determination of pourcentage of choice B depending on quantity of each juice"""
        pourcentage_A_choice_B, pourcentage_B_choice_B = [], []
        for i in range(self.ΔA + 1):
            for j in range(self.ΔB + 1):
                self.choice_A[i, j] = len(self.result_one_trial[i,j,'A'])
                self.choice_B[i, j] = len(self.result_one_trial[i,j,'B'])

        for j in range(self.ΔB, 3, -4):
            total_choice_1 = self.choice_B[(1, j)] + self.choice_A[(1, j)]
            pourcentage_A_choice_B.append((self.choice_B[(1, j)] / (total_choice_1)) * 100)
            print("total choice 1j", total_choice_1, self.choice_B[(1, j)])

            total_choice = self.choice_A[(j, 1)] + self.choice_B[(j, 1)]
            pourcentage_B_choice_B.append((self.choice_B[(j, 1)] / (total_choice)) * 100)
            print("total choice j1", total_choice, self.choice_B[(j, 1)])

        total_choice_1 = self.choice_B[(1, 0)] + self.choice_A[(1, 0)]
        total_choice_2 = self.choice_B[(0, 1)] + self.choice_A[(0, 1)]
        pourcentage_choice_B = [(self.choice_B[(1, 0)] / total_choice_1) * 100] + pourcentage_B_choice_B + pourcentage_A_choice_B[::-1] + [(self.choice_B[(0, 1)] / total_choice_2) * 100]
        print(pourcentage_choice_B)
        return pourcentage_choice_B

    def average_firing_offerB_ov(self):
        """graph 4D"""
        nb_4D = 0
        firing_4D = 0
        for j in range(self.ΔB +1):
            for i in range(self.ΔA +1):
                for choice_i in self.list_choice:
                    if len(self.result[i, j, choice_i]):
                        for k in range(2000, 3001):
                            firing_4D += self.result[(i, j, choice_i)][0][0][k]
                            nb_4D += 1
            if nb_4D != 0:
                self.firing_D.append(firing_4D / nb_4D)
            else:
                print("nb 4D = 0")
        return self.firing_D

    def average_firing_choice_cj(self):
        """graph 4H"""
        nb_4H_A, nb_4H_B = 0, 0
        firing_4H_A, firing_4H_B =0, 0
        for j in range(self.ΔB + 1):
            for i in range(self.ΔA + 1):
                if len(self.result[(i, j, 'A')]) != 0:
                    for k in range(2000, 3001):
                        firing_4H_A += self.result[(i, j, 'A')][0][1][k]
                        nb_4H_A += 1
                if len(self.result[(i,j,'B')]) != 0:
                    for k in range(2000, 3001):
                        firing_4H_B += self.result[(i, j, 'B')][0][1][k]
                        nb_4H_B += 1
                if nb_4H_A != 0:
                    self.firing_H_A.append(firing_4H_A / nb_4H_A)
                else:
                    self.firing_H_A.append(firing_4H_A)
                if nb_4H_B != 0:
                    self.firing_H_B.append(firing_4H_B / nb_4H_B)
                else:
                    self.firing_H_B.append(firing_4H_B)
        return self.firing_H_B

    def average_firing_chosen_value(self):
        """Get firing rate in function of chosen value"""
        y_a, y_b = 0, 0
        nb_Y_A, nb_Y_B = 0, 0
        for i in range(self.ΔA + 1):
            for j in range(self.ΔB + 1):
                for l in range(len(self.result_one_trial[(i, j, 'A')])):
                    self.X_A.append(i * 2)
                    for k in range(3000, 4001):
                        y_a += self.result_one_trial[(i, j, 'A')][l][4][k]
                        nb_Y_A += 1
                    self.Y_A.append(y_a / nb_Y_A)
                for l in range(len(self.result_one_trial[(i, j, 'B')])):
                    self.X_B.append(j)
                    for k in range(3000, 4001):
                        y_b += self.result_one_trial[(i, j, 'B')][l][4][k]
                        nb_Y_B += 1
                    self.Y_B.append(y_b / nb_Y_B)
        return self.X_A, self.Y_A, self.X_B, self.Y_B

    def tuning_curve_ov(self):
        mean_tuning_ov = 0
        nb_tun_ov = 0
        for i in range(self.ΔA + 1):
            for j in range(self.ΔB + 1):
                if len(self.result_one_trial[(i, j, 'A')]) > len(self.result_one_trial[(i, j, 'B')]):
                    c = 'A'
                else :
                    c = 'B'
                for l in range(len(self.result_one_trial[(i, j, c)])):
                    for k in range(2000, 3001):
                        mean_tuning_ov += self.result_one_trial[(i, j, c)][l][0][k]
                        nb_tun_ov +=1
                self.tuning_ov.append((i, j, mean_tuning_ov / nb_tun_ov, c))
        return self.tuning_ov

    def tuning_curve_cjb(self):
        mean_tuning_cjb = 0
        nb_tun_cjb = 0
        for i in range(self.ΔA + 1):
            for j in range(self.ΔB + 1):
                if len(self.result_one_trial[(i, j, 'A')]) > len(self.result_one_trial[(i, j, 'B')]):
                    c = 'A'
                else :
                    c = 'B'
                for l in range(len(self.result_one_trial[(i, j, c)])):
                    for k in range(2000, 3001):
                        mean_tuning_cjb += self.result_one_trial[(i, j, c)][l][2][k]
                        nb_tun_cjb +=1
                self.tuning_cjb.append((i, j, mean_tuning_cjb / nb_tun_cjb, c))
        return self.tuning_cjb

    def tuning_curve_cv(self):
        mean_tuning_cv = 0
        nb_tun_cv = 0
        for i in range(self.ΔA + 1):
            for j in range(self.ΔB + 1):
                if len(self.result_one_trial[(i, j, 'A')]) > len(self.result_one_trial[(i, j, 'B')]):
                    c = 'A'
                else:
                    c = 'B'
                for l in range(len(self.result_one_trial[(i, j, c)])):
                    for k in range(2000, 3001):
                        mean_tuning_cv += self.result_one_trial[(i, j, c)][l][4][k]
                        nb_tun_cv += 1
                self.tuning_cv.append((i, j, mean_tuning_cv / nb_tun_cv, c))
        return self.tuning_cv

    def firing_cja_cjb(self):
        ria, rib = 0, 0
        for i in range(self.ΔA +1):
            for j in range(self.ΔB +1):
                for choice_i in self.list_choice:
                    for l in range(len(self.result_one_trial[(i,j,choice_i)])):
                        for k in range(len(self.result_one_trial[(i,j,choice_i)][l])):
                            ria += self.result_one_trial[(i,j,choice_i)][l][1][k]
                            rib += self.result_one_trial[(i,j,choice_i)][l][2][k]
                        for p in range(8):
                            if abs(i-j) == p:
                                c = self.colour[p]
                            #if abs
                        self.offer_A.append(abs(i-j))
                        self.firing_cja.append(ria)
                        self.firing_cjb.append(rib)
        return self.offer_A, self.firing_cja, self.firing_cjb

#
