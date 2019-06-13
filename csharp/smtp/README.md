# 关于smtp  

[smtp 格式](https://help.aliyun.com/knowledge_detail/51584.html)  

## 代码  

`Program.cs`  

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using Mo.Smtp;

namespace Mo.Smtp
{
    class Program
    {
        static void Main(string[] args)
        {
            // 执行异步方法
            // 但是看不出来和同步方法有什么区别
            StartClientAsync().Wait();
        }

        public static async Task StartClientAsync()
        {
            // 获取目标地址
            int port = 25;
            IPHostEntry ipHost = Dns.GetHostEntry("mail.weichai.com");
            IPAddress ipAddress = ipHost.AddressList[0];
            IPEndPoint remoteEndPoint = new IPEndPoint(ipAddress,port);

            // 创建socket 客户端
            var client = new Socket(ipAddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp);

            bool isConnected = await client.ConnectAsync(remoteEndPoint).ConfigureAwait(false);
            if (isConnected)
            {
                // 发邮件，不全
                // 消息一起发送的话好像会比较快
                var resp = await client.ReceiveAsync().ConfigureAwait(false);
                Console.WriteLine(resp);
                var sent = await client.SendAsync("HELO domain.com\r\nauth login\r\n").ConfigureAwait(false);
                resp= await client.ReceiveAsync().ConfigureAwait(false);
                Console.WriteLine(resp);
                await client.SendAsyncBase64("user@domain.com").ConfigureAwait(false);
                await client.SendAsync("\r\n").ConfigureAwait(false);
                resp = await client.ReceiveAsync().ConfigureAwait(false);
                Console.WriteLine(resp);
                await client.SendAsyncBase64("password").ConfigureAwait(false);
                await client.SendAsync("\r\n").ConfigureAwait(false);
                resp = await client.ReceiveAsync().ConfigureAwait(false);
                Console.WriteLine(resp);
                await client.SendAsync("mail from:<user@domain.com>\r\nrcpt to:<user2@domain.com>\r\ndata\r\nsubject:Test测试\r\nfrom:12tall<user@domain.com>\r\n1111\r\n\r\n.\r\nquite\r\n").ConfigureAwait(false);
                resp = await client.ReceiveAsync().ConfigureAwait(false);
                Console.WriteLine(resp);
            }
            client.Shutdown(SocketShutdown.Both);
        }

    }
}

```

`ExSocket.cs`  

```csharp
using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

namespace Mo.Smtp
{
    public static class ExSocket
    {
        // 异步连接
        public static Task<bool> ConnectAsync(this Socket client, IPEndPoint remoteEndPoint)
        {
            if (client == null) throw new ArgumentNullException(nameof(client));
            if (remoteEndPoint == null) throw new ArgumentNullException(nameof(remoteEndPoint));

            // 以Task 运行同步方法
            return Task.Run(() => Connect(client, remoteEndPoint));
        }

        // 建立连接，同步方法
        private static bool Connect(this Socket client, EndPoint remoteEndPoint)
        {
            if (client == null || remoteEndPoint == null)
                return false;

            try
            {
                client.Connect(remoteEndPoint);
                return true;
            }
            catch (Exception)
            {
                return false;
            }
        }
        // 异步发送
        public static async Task<int> SendAsync(this Socket client, string data)
        {
            var byteData = Encoding.Default.GetBytes(data);
            return await SendAsync(client, byteData, 0, byteData.Length, 0).ConfigureAwait(false);
        }
        // 异步发送base64 编码
        public static async Task<int> SendAsyncBase64(this Socket client, string data)
        {
            var intBytes = Encoding.ASCII.GetBytes(data);
            string outStr = Convert.ToBase64String(intBytes);
            var outBytes = Encoding.ASCII.GetBytes(outStr);
            return await SendAsync(client, outBytes, 0, outBytes.Length, 0).ConfigureAwait(false);
        }
        // 最原始的发送
        private static Task<int> SendAsync(this Socket client, byte[] buffer, int offset, int size,
            SocketFlags socketFlags)
        {
            if (client == null) throw new ArgumentNullException(nameof(client));

            return Task.Run(() => client.Send(buffer, offset, size, socketFlags));
        }
        // 接收消息
        public static async Task<string> ReceiveAsync(this Socket client, int waitForFirstDelaySeconds = 30)
        {
            if (client == null) throw new ArgumentNullException(nameof(client));

            // 延时
            for (var i = 0; i < waitForFirstDelaySeconds; i++)
            {
                if (client.Available > 0)
                    break;
                await Task.Delay(1000).ConfigureAwait(false);
            }

            if (client.Available < 1)
                return null;

            // 缓冲区大小
            const int bufferSize = 1024;
            var buffer = new byte[bufferSize];

            // 获取数据
            var response = new StringBuilder(bufferSize);
            do
            {
                var size = Math.Min(bufferSize, client.Available);
                await Task.Run(() => client.Receive(buffer)).ConfigureAwait(false);
                response.Append(Encoding.ASCII.GetString(buffer, 0, size));

            } while (client.Available > 0);

            // 返回结果
            return response.ToString();
        }
    }
}
```
