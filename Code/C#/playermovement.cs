using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    public Rigidbody myRigidbody; // fixed variable name

    void Start()
    {
        myRigidbody.AddForce(transform.forward * 2500f); // use correct variable name
    }

    void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.name == "Cylinder")
        {
            print("You lose!");
        }
    }

    void FixedUpdate()
    {
        if (Input.GetKey("left") || Input.GetKey("right"))
        {
            // Check that myRigidbody has been assigned
            if (myRigidbody == null)
            {
                Debug.LogError("myRigidbody is not assigned!");
                return;
            }

            Vector3 myInput = new Vector3(Input.GetAxis("Horizontal"), 0, Input.GetAxis("Vertical"));
            myRigidbody.MovePosition(transform.position + myInput * Time.deltaTime * 5f);
        } 
    }
}
