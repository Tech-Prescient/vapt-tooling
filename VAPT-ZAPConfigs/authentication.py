"""
This script can be used by the Script Based Authentication Method to perform authentication for a given context.

To use this script, select it in the Session Properties dialog -> Authentication panel.
"""
import java.lang.String, jarray
from org.apache.commons.httpclient import URI
from org.parosproxy.paros.network import HttpRequestHeader
from org.parosproxy.paros.network import HttpHeader
from org.zaproxy.zap.network import HttpRequestBody
import os
import json
from warrant.aws_srp import AWSSRP
import requests


def remove_unicode(val):
    if isinstance(val, dict):
        return {str(k): remove_unicode(v) for k, v in val.items()}
    return str(val)


def authenticate(helper, paramsValues, credentials):
    """The authenticate function will be called for authentications made via ZAP.

    The authenticate function is called whenever ZAP requires to authenticate, for a Context for which this script was selected as the Authentication Method. The function should send any messages that are required to do the authentication and should return a message with an authenticated response so the calling method.
    NOTE: Any message sent in the function should be obtained using the 'helper.prepareMessage()' method.

    Parameters:
        helper - a helper class providing useful methods: prepareMessage(), sendAndReceive(msg)
        paramsValues - the values of the parameters configured in the Session Properties -> Authentication panel. The paramsValues is a map, having as keys the parameters names (as returned by the getRequiredParamsNames() and getOptionalParamsNames() functions below)
        credentials - an object containing the credentials values, as configured in the Session Properties -> Users panel. The credential values can be obtained via calls to the getParam(paramName) method. The param names are the ones returned by the getCredentialsParamsNames() below
    """
    print "Authenticating cognito via Jython script..."
    msg = helper.prepareMessage();

    pv = {str(k): str(v) for k, v in dict(paramsValues).items()}
    cognito_url = pv.get("cognito_url")
    cognito_user_pool_id = pv.get("cognito_user_pool_id")
    cognito_app_client_id = pv.get("cognito_app_client_id")
    username = str(credentials.getParam("username"))
    password = str(credentials.getParam("password"))

    aws = AWSSRP(
        username=username,
        password=password,
        pool_id=cognito_user_pool_id,
        client_id=cognito_app_client_id
    )

    auth_params = aws.get_auth_params()

    headers = {
        "Content-Type": "application/x-amz-json-1.1",
        "X-Amz-Target": "AWSCognitoIdentityProviderService.InitiateAuth"
    }
    payload = {
        "AuthFlow": "USER_SRP_AUTH",
        "ClientId": cognito_app_client_id,
        "AuthParameters": auth_params,
        "ClientMetadata": {}
    }
    res = requests.post(url=cognito_url, json=payload, headers=headers)
    response1 = remove_unicode(val=res.json())

    challenge = aws.process_challenge(challenge_parameters=response1["ChallengeParameters"])
    payload2 = {
        "ChallengeName": "PASSWORD_VERIFIER",
        "ClientId": cognito_app_client_id,
        "ChallengeResponses": challenge,
        "ClientMetadata": {}
    }

    requestUri = URI(cognito_url, False);
    requestMethod = HttpRequestHeader.POST;

    msg.setRequestHeader(HttpRequestHeader(requestMethod, requestUri, HttpHeader.HTTP10));
    msg.getRequestHeader().setHeader("Content-Type", "application/x-amz-json-1.1")
    msg.getRequestHeader().setHeader("X-Amz-Target", "AWSCognitoIdentityProviderService.RespondToAuthChallenge")

    msg.getRequestBody().setBody(str(json.dumps(remove_unicode(val=payload2))))
    msg.getRequestHeader().setContentLength(msg.getRequestBody().length());

    helper.sendAndReceive(msg);
    # print("msg response body", msg.getResponseBody().toString())
    print("Cognito authentication successful. Received access token. :)")

    return msg;


def getRequiredParamsNames():
    """Obtain the name of the mandatory/required parameters needed by the script.

    This function is called during the script loading to obtain a list of the names of the required configuration parameters, that will be shown in the Session Properties -> Authentication panel for configuration. They can be used to input dynamic data into the script, from the user interface (e.g. a login URL, name of POST parameters etc.)
    """
    return jarray.array(["cognito_url", "cognito_user_pool_id", "cognito_app_client_id", "aws_region"], java.lang.String);


def getOptionalParamsNames():
    """Obtain the name of the optional parameters needed by the script.

    This function is called during the script loading to obtain a list of the names of the optional configuration parameters, that will be shown in the Session Properties -> Authentication panel for configuration. They can be used to input dynamic data into the script, from the user interface (e.g. a login URL, name of POST parameters etc.).
    """
    return jarray.array([""], java.lang.String);


def getCredentialsParamsNames():
    """Obtain the name of the credential parameters needed by the script.

    This function is called during the script loading to obtain a list of the names of the parameters that are required, as credentials, for each User configured corresponding to an Authentication using this script.
    """
    return jarray.array(["username", "password"], java.lang.String);
