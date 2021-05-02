<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="TryIt.Default" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            VALIDATION SERVICE<br />
            <br />
            Input url for xml<asp:TextBox ID="TextBox1" runat="server" Width="740px"></asp:TextBox>
            <br />
            <br />
            Input url for xsd<asp:TextBox ID="TextBox2" runat="server" Width="752px"></asp:TextBox>
            <br />
            <br />
            <asp:Button ID="Button1" runat="server" Text="Verify" OnClick="Button1_Click" />
            <br />
            <br />
            output<asp:TextBox ID="TextBox3" runat="server" Width="766px"></asp:TextBox>
            <br />
            <br />
            <br />
            Xpath QUERY SERVICE<br />
            <br />
            Input url for xml<asp:TextBox ID="TextBox4" runat="server" Width="786px"></asp:TextBox>
            <br />
            <br />
            Input xpath query<asp:TextBox ID="TextBox5" runat="server" Width="783px"></asp:TextBox>
            <br />
            <br />
            <asp:Button ID="Button2" runat="server" Text="get query output" OnClick="Button2_Click" />
            <br />
            <br />
            output<br />
            <br />
            <asp:ListBox ID="ListBox1" runat="server" Height="337px" Width="763px"></asp:ListBox>
        </div>
    </form>
</body>
</html>
