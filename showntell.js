// Design a simple authentication system for a command-line application. The system should allow users to register with a username and password, 
// and then log in using their credentials.
//  Store the user credentials in a dictionary and ensure that passwords are checked securely without storing them in plain text in your code

class Authenticate{
  constructor(){
    this.authenticatation_details = []
  }

 register(){
  let alphanumeric = /[a-z0-9]/;
  const credentials = {username:username,password:password}
  if(credentials.password.match(alphanumeric)){
    this.authenticatation_details.push(credentials)
    console.log("Password set successfully");
  }

  else{
   user(!password.match(alphanumeric))
   console.log("password should contain letters and symbols");                                                                     
                                                                                                                                                                                                                                                                    
  }
 } 
}


const userAuthentication = new Authenticate()
Authenticate.register(username, password);
const username = "waluse"
const password = "wal45"
