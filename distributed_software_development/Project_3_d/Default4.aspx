<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default4.aspx.cs" Inherits="Homework3_4.Default4" %>

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
    <form id="form1" runat="server">
        <p style="height: 33px">
            NEWS SERVICE</p>
        <p style="height: 33px">
            Input: List of comma separated topics (String)&nbsp;
            <asp:TextBox ID="TextBox7" runat="server" OnTextChanged="TextBox7_TextChanged"></asp:TextBox>
&nbsp;&nbsp;
        </p>
        <p style="height: 33px">
            Example input: tesla,qualcomm,america&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        </p>
        <p style="height: 38px">
&nbsp;
            <asp:Button ID="Button3" runat="server" OnClick="Button3_Click" Text="Get News" />
        </p>
        <p style="height: 38px">
            &nbsp;</p>
        <p style="height: 38px">
            Output: List of news link related to the area , separated by topics</p>
        <p style="height: 36px">
            <asp:ListBox ID="ListBox1" runat="server" Height="203px" Width="1030px"></asp:ListBox>
        </p>
        <p style="height: 36px">
            &nbsp;</p>
        <p style="height: 36px">
            &nbsp;</p>
        <p style="height: 36px">
            &nbsp;</p>
        <p style="height: 36px">
            &nbsp;</p>
        <p class="auto-style1" style="height: 36px">
            <asp:Button ID="Button4" runat="server" OnClick="Button4_Click" Text="Back/Home" />
        </p>
        <p style="height: 36px">
            &nbsp;</p>
        <div>
        </div>
    </form>
</body>
</html>
