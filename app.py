from q1_max_mfr import max_mfr
from max_mfr_combined import max_mfr_combined
from q2_top_average import top_average
from q3_good_bad_fe import good_bad_fe
from df_combined_year import *
from good_bad_fe_combined import good_bad_fe_combined
from q4_wheel_engine import wheel_engine
from wheel_engine_combined import wheel_engine_combined
from drive_fe import drive_fe
from corr_release_day import corr_release_day
from corr_fe_co2 import corr_fe_co2

class Router:
    def __init__(self):
        self.running = True

    def run(self):
        self.logo()
        self.command_view()
        while self.running:
            choice = str(input('Please choose the option from the <main menu> above. Input the option number: '))
            if choice == '1':
                print('Please select the period for your choice. \n')
                print('<option 1>: Year 2015 figures \n<option 2>: Year 2015 to Year 2023 (9 years) figures \n')
                option = str(input('Input the option number: \n'))
                if option == '1':
                    max_mfr()
                elif option == '2':
                    max_mfr_combined()
                else:
                    print('You have input wrong number.')
            elif choice == '2':
                top_average()
            elif choice == '3':
                print('Please select the period for your choice. \n')
                print('<option 1>: Year 2015 figures \n<option 2>: Year 2015 to Year 2023 (9 years) figures \n')
                option = str(input('Input the option number: \n'))
                if option == '1':
                    good_bad_fe()
                elif option == '2':
                    good_bad_fe_combined(df_all_years)
                else:
                    print('You have input wrong number.')
            elif choice == '4':
                print('Please select the period for your choice. \n')
                print('<option 1>: Year 2015 figures \n<option 2>: Year 2015 to Year 2023 (9 years) figures \n')
                option = str(input('Input the option number: \n'))
                if option == '1':
                    wheel_engine()
                elif option == '2':
                    wheel_engine_combined()
                else:
                    print('You have input wrong number.')
            elif choice == '5':
                print('<The result is based on year 2015 data only>')
                drive_fe()
            elif choice == '6':
                print('<The result is based on year 2015 to 2023 (9 years) figures \n>')
                corr_release_day(df_all_years)
            elif choice == '7':
                print('<The result is based on year 2015 data only>')
                corr_fe_co2()
            else:
                print('See you next time!')
                self.running = False



    def command_view(self):
        print('1. Find the car manufacturer which contains most quantity of car models. ')
        print('2. Find the top average fuel economy for the city and highway driving from the given dataset. ')
        print('3. Find good and bad average fuel economy cars from all transmission types. ')
        print('4. Find car manufacturers which have 4WD and 2WD with engine power is more than 3.5')
        print('5. Find the fuel economy performance among different drive type (e.g. front wheel vs all wheel).')
        print('6. Show the correlations between fuel economy and car release day for all years. ')
        print('7. Show the correlations between fuel economy and different types of co2 and engine power. ')

    def logo(self):
        print('---------------------------------------------------------------------------------')
        print('')
        print('Welcome to explore the data analysis for the automobile research company.')
        print('')
        print('---------------------------------------------------------------------------------')


app = Router()
app.run()
