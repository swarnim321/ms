<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="Homework5.Default" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        .auto-style1 {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <p>
        <strong>RECOMMENDATION SERVICE FOR RENEWABLE ENERGY</strong></p>
    <form id="form1" runat="server">
        <p>
            &nbsp;</p>
        <p>
            <strong>Enter Zip code (Ex: 85281)</strong> &nbsp;
            <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;</p>
        <p>
            <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" Text="Get Solar/Wind Index and Recommendation and Related News" />
        </p>
        <p>
            Solar index<asp:TextBox ID="TextBox2" runat="server"></asp:TextBox>
        </p>
        <p>
            Recommendation for setting up solar farm <asp:TextBox ID="TextBox3" runat="server" Width="503px"></asp:TextBox>
        </p>
        <p>
            &nbsp;</p>
        <p>
            Wind Index<asp:TextBox ID="TextBox5" runat="server"></asp:TextBox>
        </p>
        <p>
            Recommendation for setting up wind farm <asp:TextBox ID="TextBox6" runat="server" Width="556px"></asp:TextBox>
        </p>
        <p>
            &nbsp;</p>
        <p class="auto-style1">
            News related to Solar/Wind energy</p>
        <p>
            <asp:ListBox ID="ListBox1" runat="server" Height="275px" Width="617px"></asp:ListBox>
        </p>
        <p>
            &nbsp; Zip code searched in this session (through<strong> session </strong>variable)&nbsp;
            <asp:TextBox ID="TextBox8" runat="server"></asp:TextBox>
        &nbsp;&nbsp; </p>
        <p>
            <strong>Cached </strong>result of last used zip code</p>
        <p>
            <asp:ListBox ID="ListBox3" runat="server" Height="92px" Width="263px"></asp:ListBox>
        </p>
        <p>
            &nbsp;</p>
        <p>
            <strong>Enter topic (in comma separated form) to get the news on more topics : Ex (america,renewable,corona)</strong>
            <asp:TextBox ID="TextBox7" runat="server" Width="756px"></asp:TextBox>
        </p>
        <p>
            <asp:Button ID="Button3" runat="server" OnClick="Button3_Click" Text="Get further News" />
        </p>
        <p>
            News link for the searched topics</p>
        <p>
            <asp:ListBox ID="ListBox2" runat="server" Height="289px" Width="647px"></asp:ListBox>
        </p>
        <div>
        </div>
    </form>
</body>
</html>
