# while self.comando in '@><=+-0':
#     if self.ligada == False:           #TV ligada
#         print('TV desligada')
#         self.comando = str(input('A TV está desligada - Use @ para ligá-la: (0 encerrar programa) '))
#         if self.comando not in '@><-+0':
#             print('Comando inválido. Tente novamente')
#             self.comando = str(input('A TV está desligada - Use @ para ligá-la: (0 encerrar programa) '))
#         elif self.comando == '@':
#             self.ligada = True
#         elif self.comando == '0':
#             break
#
#     elif self.ligada == True:
#         print('TV ligada')
#         self.comando = str(input(f'< CH{self.canal_atual} >   - VOL{self.volume} + '))
#
#         if self.comando not in '@><-+':
#             print('Comando inválido. Tente novamente')
#             self.comando = str(input('A TV está desligada - Use @ para ligá-la: '))
#
#         match self.comando:
#             case '<':
#
#
#             case '>':
#                 if self.canal_atual == self.canal_maximo:
#                     self.canal_atual = self.canal_minimo
#                 else:
#                     self.canal_atual += 1
#
#             case '-':
#                 if self.volume == self.volume_minimo:
#                     self.volume = self.volume_minimo
#                 else:
#                     self.volume -= 1
#             case '+':
#                if self.volume == self.volume_maximo:
#                    self.volume = self.volume_maximo
#                else:
#                    self.volume += 1
#             case '@':
#                 self.ligada = False