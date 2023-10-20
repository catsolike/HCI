namespace WinFormsApp1
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            label1=new Label();
            FirstName=new TextBox();
            LastName=new TextBox();
            label2=new Label();
            Phone=new TextBox();
            label3=new Label();
            Email=new TextBox();
            label4=new Label();
            Save=new Button();
            ErrorMessage=new Label();
            textBox1=new TextBox();
            Gender=new Label();
            label5=new Label();
            textBox2=new TextBox();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize=true;
            label1.Location=new Point(30, 29);
            label1.Margin=new Padding(1, 0, 1, 0);
            label1.Name="label1";
            label1.Size=new Size(64, 15);
            label1.TabIndex=0;
            label1.Text="First Name";
            // 
            // FirstName
            // 
            FirstName.Location=new Point(30, 50);
            FirstName.Margin=new Padding(1);
            FirstName.Name="FirstName";
            FirstName.Size=new Size(228, 23);
            FirstName.TabIndex=1;
            // 
            // LastName
            // 
            LastName.Location=new Point(30, 108);
            LastName.Margin=new Padding(1);
            LastName.Name="LastName";
            LastName.Size=new Size(228, 23);
            LastName.TabIndex=3;
            // 
            // label2
            // 
            label2.AutoSize=true;
            label2.Location=new Point(30, 86);
            label2.Margin=new Padding(1, 0, 1, 0);
            label2.Name="label2";
            label2.Size=new Size(63, 15);
            label2.TabIndex=2;
            label2.Text="Last Name";
            // 
            // Phone
            // 
            Phone.Location=new Point(30, 224);
            Phone.Margin=new Padding(1);
            Phone.Name="Phone";
            Phone.Size=new Size(228, 23);
            Phone.TabIndex=7;
            // 
            // label3
            // 
            label3.AutoSize=true;
            label3.Location=new Point(30, 208);
            label3.Margin=new Padding(1, 0, 1, 0);
            label3.Name="label3";
            label3.Size=new Size(41, 15);
            label3.TabIndex=6;
            label3.Text="Phone";
            // 
            // Email
            // 
            Email.Location=new Point(30, 167);
            Email.Margin=new Padding(1);
            Email.Name="Email";
            Email.Size=new Size(228, 23);
            Email.TabIndex=5;
            // 
            // label4
            // 
            label4.AutoSize=true;
            label4.Location=new Point(30, 145);
            label4.Margin=new Padding(1, 0, 1, 0);
            label4.Name="label4";
            label4.Size=new Size(36, 15);
            label4.TabIndex=4;
            label4.Text="Email";
            label4.Click+=label4_Click;
            // 
            // Save
            // 
            Save.Location=new Point(181, 410);
            Save.Margin=new Padding(1);
            Save.Name="Save";
            Save.Size=new Size(77, 21);
            Save.TabIndex=8;
            Save.Text="Save";
            Save.UseVisualStyleBackColor=true;
            Save.Click+=Save_Click;
            // 
            // ErrorMessage
            // 
            ErrorMessage.AutoSize=true;
            ErrorMessage.ForeColor=Color.Red;
            ErrorMessage.Location=new Point(30, 352);
            ErrorMessage.Margin=new Padding(1, 0, 1, 0);
            ErrorMessage.Name="ErrorMessage";
            ErrorMessage.Size=new Size(0, 15);
            ErrorMessage.TabIndex=9;
            // 
            // textBox1
            // 
            textBox1.Location=new Point(30, 328);
            textBox1.Name="textBox1";
            textBox1.Size=new Size(228, 23);
            textBox1.TabIndex=10;
            // 
            // Gender
            // 
            Gender.AutoSize=true;
            Gender.Location=new Point(30, 310);
            Gender.Name="Gender";
            Gender.Size=new Size(45, 15);
            Gender.TabIndex=11;
            Gender.Text="Gender";
            Gender.Click+=label5_Click;
            // 
            // label5
            // 
            label5.AutoSize=true;
            label5.Location=new Point(30, 261);
            label5.Name="label5";
            label5.Size=new Size(102, 15);
            label5.TabIndex=12;
            label5.Text="Place of residence";
            // 
            // textBox2
            // 
            textBox2.Location=new Point(30, 279);
            textBox2.Name="textBox2";
            textBox2.Size=new Size(228, 23);
            textBox2.TabIndex=13;
            // 
            // Form1
            // 
            AutoScaleDimensions=new SizeF(7F, 15F);
            AutoScaleMode=AutoScaleMode.Font;
            ClientSize=new Size(329, 452);
            Controls.Add(textBox2);
            Controls.Add(label5);
            Controls.Add(Gender);
            Controls.Add(textBox1);
            Controls.Add(ErrorMessage);
            Controls.Add(Save);
            Controls.Add(Phone);
            Controls.Add(label3);
            Controls.Add(Email);
            Controls.Add(label4);
            Controls.Add(LastName);
            Controls.Add(label2);
            Controls.Add(FirstName);
            Controls.Add(label1);
            Margin=new Padding(1);
            Name="Form1";
            Text="Form1";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private TextBox FirstName;
        private TextBox LastName;
        private Label label2;
        private TextBox Phone;
        private Label label3;
        private TextBox Email;
        private Label label4;
        private Button Save;
        private Label ErrorMessage;
        private TextBox textBox1;
        private Label Gender;
        private Label label5;
        private TextBox textBox2;
    }
}