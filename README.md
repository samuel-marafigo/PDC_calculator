1. Introduction

 
This project, initiated during my pharmacy post-graduate residency program, is an intersection between my experience in pharmacy and software development. The core objective is to use Python to calculate the pharmacotherapy adherence measure known as Proportion of Days Covered (PDC) based on dispensation dates registered in a database, specifically a CSV file.
As pharmacies focus heavily on traceability, they each generate vast amounts of data. This opens up the possibility of large-scale, data-driven adherence studies. Adherence studies strive to find patterns of adherence to pharmacotherapy, which, in turn, is heavily linked to positive clinical outcomes in the literature.
According to the Pharmacy Quality Alliance (2023), PDC is the preferred measure of adherence for chronic illness treatments. The definition of PDC as PDC = (Sum of days covered in time frame) ÷ (number of days in time frame) × 100 does not convey the complexity behind its calculation. As observed by Canfield et al (2019), this model considers patient prescription refill (or dispensation) dates and quantities, and tracks the number of days they were "covered" by medication in a given period, also accounting for any surplus that the patient may acquire, thus requiring automation for the calculations.
The motivation for this project stems from a gap in the field; despite many authors reporting results of PDC calculation, there seems to be a lack of publicly available PDC calculators. By creating a solution that could be applied locally without relying on third-party assistance, I was able to manage the risk of data leaks, a key point for getting the approval of an Ethics Committee.
Initially, I prompted ChatGPT numerous times to create the main logic behind it using the definition of PDC provided by Canfield et al (2019), and compared the calculation results to my test data, where I had calculated different scenarios by hand.
While the initial code is functional, as part of my ongoing learning and portfolio building, I plan on adding new features and refactoring it to align with IT best practices, such as code modularity and extensive testing, improving on the work initially done by ChatGPT.


2. Getting started

   
The project is being developed using Python 3.9 and currently no dependencies are needed.


3. Features and documentation

   
The application currently features a function for calculating the PDC and a function for writing the results to a new csv. There is no user interface and paths must be specified directly into the functions. 
In it's initial state, it expects a csv file with the following columns: Data da Saída;Usuário;Sexo;Idade;Quantidade;Farmacêutico;Cenário.
The column layout is based on the csv exported from the database it was originally designed for. 
To use the application, the user must execute main.py and call the functions as such:
PDC, user_medication = calculate_PDC('your_data.csv')
write_PDC_to_file('your_data.csv', 'PDC_output.csv', PDC, user_medication)


4. Roadmap

1)Add a menu-based user interface
2)Make the code less dependent on the format of the file
3)Make it possible for the user to change the parameters of the calculations, such as inclusion and exclusion criteria


5. Acknowlodgements


The first version of this code and logic behind it, while I had very little experience with practical programming, was made possible by OpenAI's ChatGPT.


4. License

   
This project is licensed under the GNU General Public License v3.0.


5. Contact information

    
All kinds of feedback, comments or requests are always welcome!
You may reach me through the following:
Email: swmarafigo@gmail.com // Linkedin: https://www.linkedin.com/in/swmarafigo/ // Discord: swmarafigo


6. Changelog

    
Version 0.1.0 - Initial version.


   
