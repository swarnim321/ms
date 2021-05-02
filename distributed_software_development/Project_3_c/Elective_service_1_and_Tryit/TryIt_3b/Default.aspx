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
            <asp:Label ID="Label3" runat="server" Text="DESCRIPTION: Get Wind index of an area by entering the zip code."></asp:Label>
            <br />
            <br />
            <asp:Label ID="Label6" runat="server" Text="Note: The zipcode will be verified and converted to lat/lon coordinates at the back end to ease user experience."></asp:Label>
            <br />
            <br />
            <br />
            <asp:Label ID="Label5" runat="server" Text="URL OF THE SERVICE:  http://localhost:62609/Service1.svc/wind/zip?input={zip code}"></asp:Label>
            <br />
            <br />
            <asp:Label ID="Label1" runat="server" Text="Enter the ZIP CODE to get the wind index  (INTEGER INPUT): "></asp:Label>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <asp:TextBox ID="zip_input" runat="server"></asp:TextBox>
            <br />
            <br />
            <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" Text="Get Wind Index" />
            <br />
            <br />
            <br />
            <br />
            <asp:Label ID="Label4" runat="server" Text="The Wind index of the area is returned in DOUBLE format along with a recommendation good/bad (STRING format) below:"></asp:Label>
            <br />
            <br />
            <asp:Label ID="Label2" runat="server" Text="Wind_Index"></asp:Label>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <asp:TextBox ID="output_box" runat="server" Width="214px"></asp:TextBox>
            <br />
            <br />
            <br />
            <asp:Label ID="Label7" runat="server" Text="Recommendation"></asp:Label>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <asp:TextBox ID="TextBox1" runat="server" Width="290px"></asp:TextBox>
            <br />
            <br />
        </div>
    </form>
</body>
</html>
