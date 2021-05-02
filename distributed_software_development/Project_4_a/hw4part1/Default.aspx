<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="hw4part1.Default" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <p>
        XML READING</p>
    <p>
        URL for the XML (try <a href="http://webstrar48.fulton.asu.edu/page6/restaurants.xml">http://webstrar48.fulton.asu.edu/page6/restaurants.xml</a> for tsting)</p>
    <form id="form1" runat="server">
        <p>
            <br />
            <asp:TextBox ID="TextBox1" runat="server" Width="787px"></asp:TextBox>
        </p>
        <p>
            &nbsp;</p>
        <p>
            <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" Text="View contents of XML" />
        </p>
        <p>
            <asp:ListBox ID="ListBox1" runat="server" Height="455px" Width="623px"></asp:ListBox>
        </p>
        <div>
        </div>
    </form>
</body>
</html>
