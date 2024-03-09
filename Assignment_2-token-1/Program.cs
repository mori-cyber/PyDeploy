var client = new HttpClient();
var request = new HttpRequestMessage(HttpMethod.Get, "https://www.fruityvice.com/api/fruit/banana");
var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());
