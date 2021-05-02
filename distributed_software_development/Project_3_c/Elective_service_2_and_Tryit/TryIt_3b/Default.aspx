<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="TryIt_3b.TryIt" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <br />
            <asp:Label ID="Label3" runat="server" Text="DESCRIPTION: Get list of news url for the topics entered in the input box"></asp:Label>
            <br />
            <br />
            <asp:Label ID="Label5" runat="server" Text="URL OF THE SERVICE:  http://localhost:62610/Service1.svc/news/{list of input string}"></asp:Label>
            <br />
            <br />
            <asp:Label ID="Label1" runat="server" Text="Enter the topics to ge the related urls , WITHOUT SPACES  (COMMA SEPARATED STRING INPUT): "></asp:Label>
&nbsp;<br />
            &nbsp;&nbsp;&nbsp;&nbsp;<br />
            <asp:Label ID="Label6" runat="server" Text="Example input: tesla,qualcomm"></asp:Label>
            <br />
            <br />
            <br />
&nbsp;<asp:TextBox ID="zip_input" runat="server" Width="703px"></asp:TextBox>
            <br />
            <br />
            <br />
            <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" Text="Get news URL for topics" />
            <br />
            <br />
            <asp:ListBox ID="ListBox1" runat="server" Height="412px" OnSelectedIndexChanged="ListBox1_SelectedIndexChanged" Width="1231px"></asp:ListBox>
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            <br />
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <br />
            <br />
            <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <br />
            <br />
        </div>
    </form>
</body>
</html>
