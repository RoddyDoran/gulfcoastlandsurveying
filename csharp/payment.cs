var client = new HttpClient();
var request = new HttpRequestMessage(HttpMethod.Post, "https://api.payarc.net/v1/charges");
request.Headers.Add("Accept", "application/json");
request.Headers.Add("Authorization", "Bearer {{eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxNjQ4NSIsImp0aSI6IjE5ZjdmMTI1MmEzNDg0NTc4OTMwYWE2Y2VhYTFiNzdmNWVmNGUxZTQ2NWIwY2ZmMDgwYjdmMDYwODUxYWNkNGY1Y2I4NmE4M2RjMmE2MTcwIiwiaWF0IjoxNzEyNzkzNTAwLCJuYmYiOjE3MTI3OTM1MDAsImV4cCI6MTg3MDQ3MzUwMCwic3ViIjoiMzM3NjUiLCJzY29wZXMiOiIqIn0.W4lOdTAIeU7rF-lXWoHnyhVXAgmkPm8j_P3V3jvD3GLjgQP61isMA6ZtBzVKbgUWCE7h-8XkgU1_2x6T4NImVqLqf4drtU-CL1w_qTF54gC1YdPfHnUInsiG14dZ3m2k0HgM_GfE7rcUTqVr-RLPGZCDzfrljmdu5S9pgFM_bEt-QFpFo5D829hqS3gIAzavg8pgV8lcJaAj_qJOAWZozts5a8a9MbSSF6PdubJrfJjL9X87BEbx14EahpCbfkkcX7eDD9T_SGuxU0GcexsMpm3mFSxMF2VFFdWCIh5lAn-DL7DBNqXE0wKJgQ5eafW9t4ywN-iLzbxxDddAn7uMaby8MCw3KqSG24z8JMR3exr2FhSI4a1SqT21CYfo0RM9XpQ9wkqAe9HSfYzQ4xGHxCHbez0Vuu98zxXUndMcLLCG-_ZeVFDBgvkaeiaTzHvxObtO_h2KHXVNl5PBNn7t81DHWtf9SysXgZBqZZYkFKNX92iVA2Dwh6WepzpAg73ixGJzAN_XYfR_M3L5dLVPwSjLFAIqRHR5HrE6RRqFraBhtmt0zIggi7GNgaebEbWbnEGaDC6zn6XXeEZT17EQPkU1wM4rGzGEBjl5HrAr7R4EDX0stYHMqkN7TM6hQ9Qbn8mSc8hicRtPA92cVeiJDEHmN0OmvymxOPnLHbfwLwk}}");

var collection = new List<KeyValuePair<string, string>> {
    new("amount", "1201"),
    new("currency", "usd"),
    new("statement_description", "statement description"),
    new("token_id", token),  // Token from Python
    new("email", email),  // Email from Python
    new("capture", "1")
};

request.Content = new FormUrlEncodedContent(collection);
var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());
