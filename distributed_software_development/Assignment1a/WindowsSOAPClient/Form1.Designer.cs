
namespace WindowsSOAPClient
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.input_Textbox = new System.Windows.Forms.TextBox();
            this.output_Textbox = new System.Windows.Forms.MaskedTextBox();
            this.vowels_Button = new System.Windows.Forms.Button();
            this.count_Uppercase_button = new System.Windows.Forms.Button();
            this.reverse_Button = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // input_Textbox
            // 
            this.input_Textbox.Location = new System.Drawing.Point(150, 28);
            this.input_Textbox.Name = "input_Textbox";
            this.input_Textbox.Size = new System.Drawing.Size(205, 26);
            this.input_Textbox.TabIndex = 0;
            // 
            // output_Textbox
            // 
            this.output_Textbox.Location = new System.Drawing.Point(150, 321);
            this.output_Textbox.Name = "output_Textbox";
            this.output_Textbox.Size = new System.Drawing.Size(226, 26);
            this.output_Textbox.TabIndex = 1;
            // 
            // vowels_Button
            // 
            this.vowels_Button.Location = new System.Drawing.Point(31, 83);
            this.vowels_Button.Name = "vowels_Button";
            this.vowels_Button.Size = new System.Drawing.Size(160, 47);
            this.vowels_Button.TabIndex = 2;
            this.vowels_Button.Text = "Count Vowels";
            this.vowels_Button.UseVisualStyleBackColor = true;
            this.vowels_Button.Click += new System.EventHandler(this.vowels_Button_Click);
            // 
            // count_Uppercase_button
            // 
            this.count_Uppercase_button.Location = new System.Drawing.Point(31, 155);
            this.count_Uppercase_button.Name = "count_Uppercase_button";
            this.count_Uppercase_button.Size = new System.Drawing.Size(156, 56);
            this.count_Uppercase_button.TabIndex = 3;
            this.count_Uppercase_button.Text = "Count Uppercase letters";
            this.count_Uppercase_button.UseVisualStyleBackColor = true;
            this.count_Uppercase_button.Click += new System.EventHandler(this.count_Uppercase_button_Click);
            // 
            // reverse_Button
            // 
            this.reverse_Button.Location = new System.Drawing.Point(34, 238);
            this.reverse_Button.Name = "reverse_Button";
            this.reverse_Button.Size = new System.Drawing.Size(153, 45);
            this.reverse_Button.TabIndex = 4;
            this.reverse_Button.Text = "Reverse String";
            this.reverse_Button.UseVisualStyleBackColor = true;
            this.reverse_Button.Click += new System.EventHandler(this.reverse_Button_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(48, 34);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(92, 20);
            this.label1.TabIndex = 5;
            this.label1.Text = "Input String";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(40, 327);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(58, 20);
            this.label2.TabIndex = 6;
            this.label2.Text = "Output";
            this.label2.Click += new System.EventHandler(this.label2_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.reverse_Button);
            this.Controls.Add(this.count_Uppercase_button);
            this.Controls.Add(this.vowels_Button);
            this.Controls.Add(this.output_Textbox);
            this.Controls.Add(this.input_Textbox);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox input_Textbox;
        private System.Windows.Forms.MaskedTextBox output_Textbox;
        private System.Windows.Forms.Button vowels_Button;
        private System.Windows.Forms.Button count_Uppercase_button;
        private System.Windows.Forms.Button reverse_Button;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
    }
}

