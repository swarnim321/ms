<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="Homework3_4.Default" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        .auto-style1 {
            width: 100%;
        }
        .auto-style2 {
            width: 289px;
        }
        .auto-style3 {
            width: 335px;
        }
        .auto-style4 {
            width: 392px;
        }
        .auto-style5 {
            width: 335px;
            height: 82px;
            text-decoration: underline;
            color: #008080;
        }
        .auto-style6 {
            width: 289px;
            height: 82px;
        }
        .auto-style7 {
            width: 392px;
            height: 82px;
            text-decoration: underline;
            color: #008080;
        }
        .auto-style8 {
            height: 82px;
        }
        .auto-style10 {
            text-decoration: underline;
            color: #008080;
        }
        .auto-style11 {
            font-weight: normal;
        }
        .auto-style12 {
            color: #008080;
        }
        .auto-style13 {
            color: #0000FF;
        }
        .auto-style14 {
            color: #800080;
        }
        .auto-style15 {
            height: 82px;
            width: 74px;
        }
        .auto-style16 {
            width: 74px;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
        <p style="height: 36px">
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span class="auto-style14"><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; SERVICE DIRECTORY</strong></span></p>
        <p style="height: 36px">
            Project developed by: <span class="auto-style13">SWARNIM SINHA</span></p>
        <div>
        </div>
        <table class="auto-style1">
            <tr>
                <td class="auto-style5"><strong class="auto-style11"><strong>Service name with input and output types</strong></strong></td>
                <td class="auto-style6"><span class="auto-style12"><strong>&nbsp;&nbsp; </strong></span><span class="auto-style10"><strong>Try It&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Link</strong></span></td>
                <td class="auto-style7"><strong>Service Description</strong></td>
                <td class="auto-style15">&nbsp;</td>
                <td class="auto-style8"><strong>&nbsp;&nbsp;&nbsp;&nbsp; <span class="auto-style10">APIs/Web service method</span></strong></td>
            </tr>
            <tr>
                <td class="auto-style3"><em>
                    <br />
                    Solar service</em><br />
                    <strong>input</strong>: US Zip code (Integer)<br />
                    <strong>output</strong>: Solar index (double)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; recommendation(String)</td>
                <td class="auto-style2">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <asp:Button ID="Button4" runat="server" OnClick="Button4_Click" Text="Try_It" />
                </td>
                <td class="auto-style4">
                    <br />
                    It takes a zip code as an input and returns the average annual solar index of the area along with a recommendation if the area is good for setting up solar farms.</td>
                <td class="auto-style16">&nbsp;</td>
                <td>&nbsp;&nbsp;&nbsp; &quot;<a href="http://webstrar48.fulton.asu.edu/page7/Service1.svc/solar/zip?input=">http://webstrar48.fulton.asu.edu/page7/Service1.svc/solar/zip?&nbsp; input=</a>&quot;+zip<br />
                    <br />
&nbsp;&nbsp;&nbsp;&nbsp; Ex: http://webstrar48.fulton.asu.edu/page7/Service1.svc/solar/zip?input=85281</td>
            </tr>
            <tr>
                <td class="auto-style3">
                    <br />
                    <em>Wind service</em><br />
                    <strong>input</strong>: US Zip code (Integer)<br />
                    <strong>output</strong>: Wind index (double)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; recommendation(String)</td>
                <td class="auto-style2">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <asp:Button ID="Button5" runat="server" OnClick="Button5_Click" Text="Try_It" />
                    &nbsp;</td>
                <td class="auto-style4">
                    <br />
                    It takes a zip code as an input and returns the average annual solar index of the area along with a recommendation if the area is good for setting up solar farms.</td>
                <td class="auto-style16">&nbsp;</td>
                <td>&nbsp;&nbsp;&nbsp; &quot;<a href="http://webstrar48.fulton.asu.edu/page8/Service1.svc/wind/zip?input=">http://webstrar48.fulton.asu.edu/page8/Service1.svc/wind/zip?input=</a>&quot;+zip<br />
                    <br />
&nbsp;&nbsp;&nbsp; Ex: http://webstrar48.fulton.asu.edu/page7/Service1.svc/wind/zip?input=85281</td>
            </tr>
            <tr>
                <td class="auto-style3">
                    <br />
                    <em>News service</em><br />
                    <strong>input</strong>: List of topics (Comma separated string) Ex: Tesla,qualcomm<br />
                    <strong>output</strong>: list of news link related to the topic</td>
                <td class="auto-style2">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <asp:Button ID="Button6" runat="server" OnClick="Button6_Click" Text="Try_It" />
                    &nbsp;</td>
                <td class="auto-style4">It takes&nbsp; input , a list of comma separated value as topics and returns the list of news link separated by topics as the output.</td>
                <td class="auto-style16">&nbsp;</td>
                <td>&nbsp;&nbsp; &quot;<a href="http://webstrar48.fulton.asu.edu/page9/Service1.svc/news/">http://webstrar48.fulton.asu.edu/page9/Service1.svc/news/</a>&quot;+topics<br />
                    <br />
&nbsp;&nbsp;&nbsp; Ex: http://webstrar48.fulton.asu.edu/page9/Service1.svc/news/tesla,qualcomm</td>
            </tr>
        </table>
    </form>
</body>
</html>
