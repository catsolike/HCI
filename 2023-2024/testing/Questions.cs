using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class Questions
    {
        private string firstname;
        private string lastname;
        private string email;
        private string phone;
        private string placeofresidence;
        private char gender;

        private bool nullvalidate(string value)
        {
            return !(value == null || value.Length < 2);
        }

        private bool uppercasevalidate(string value)
        {
            return (char.IsUpper(value[0]));
        }

        private void namevalidate(string value)
        {
            if (!nullvalidate(value))
            {
                throw new ArgumentException("value is null or empty");
            }

            if (!uppercasevalidate(value))
            {
                throw new ArgumentException("value must start with upper case");
            }
        }
        public string Firstname
        {
            get { return firstname; }
            set 
            {
                namevalidate(value);
                firstname = value; 
            }
        }
        public string Lastname
        {
            get { return lastname; }
            set
            {
                namevalidate(value);
                lastname = value;
            }
        }
        public string Email
        {
            get { return email; }
            set
            {
                var sign = System.Text.RegularExpressions.Regex.Match(value, "^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$");
                if (sign == null)
                {
                    throw new ArgumentException("mail invalid!");
                }
                email = value;
        
            }
        }
        public string Phone
        {
            get { return phone; }
            set
            {
                if (!nullvalidate(value))
                {
                    throw new ArgumentNullException("value is null");
                }
                if (value[0] != '8' || (value[0] != '+' && value[1] != '7'))
                {
                    throw new ArgumentException("phone must starts with '+7' or '8'");
                }
                phone = value;
            }
        }

        public string Placeofresidence
        {
            get { return placeofresidence; }
            set { placeofresidence = value; }
            // Хз как проверить местожительство Россия
        }

        public char Gender
        {
            get { return gender; }
            set 
            {
                if (value != 'м' & value != 'ж')
                {
                    throw new ArgumentException("gender should be 'м' or 'ж'");
                }
                Console.WriteLine(value);
                gender = value;
            }
        }

    }
}
