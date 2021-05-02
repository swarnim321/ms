<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default2.aspx.cs" Inherits="Homework3_4.Default2" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        .auto-style1 {
            margin-left: 480px;
        }
    </style>
</head>
<body>
    <p>
        <br />
    </p>
    <form id="form1" runat="server">
        <p style="height: 33px">
            SOLAR SERVICE</p>
        <p style="height: 33px">
            Input: Zip code (integer)
            <asp:TextBox ID="TextBox1" runat="server" OnTextChanged="TextBox1_TextChanged"></asp:TextBox>
&nbsp;&nbsp;&nbsp;&nbsp;
        </p>
        <p style="height: 33px">
            Example input: 85281&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        </p>
        <p style="height: 38px">
&nbsp;
            <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" Text="Get Solar Index" />
        </p>
        <p style="height: 36px">
            Output: Solar index (double)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <asp:TextBox ID="TextBox2" runat="server" OnTextChanged="TextBox2_TextChanged" Width="318px"></asp:TextBox>
        </p>
        <p style="height: 36px">
            Output: Recommendation (String)&nbsp;&nbsp;
            <asp:TextBox ID="TextBox3" runat="server" OnTextChanged="TextBox3_TextChanged" Width="405px"></asp:TextBox>
        </p>
        <p style="height: 36px">
            &nbsp;</p>
        <p class="auto-style1" style="height: 36px">
            <asp:Button ID="Button2" runat="server" OnClick="Button2_Click" Text="Back/Home" />
        </p>
        <p style="height: 36px">
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;</p>
        <div>
        </div>
    </form>
</body>
</html>
