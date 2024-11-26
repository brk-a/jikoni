# Exploratory Testing Report for Jumia Website
Tester Name: [F Njakai][def2] <br/>
Date of Testing: Tue, 26 Nov, 2024 <br/>
Website URL: [https://www.jumia.co.ke/][def] <br/>
Testing Duration: Approximately 3 hours <br/>
Purpose: Test key functionalities of the Jumia website from a user perspective <br/>
### Test Case Results
| Test Case ID | Test Description | Steps taken | Expected Result | Actual Result | Status | Notes |
|:---------------|:----------------------|:---------------------------------------|:----------------------------------|:----------------------------------|:--------|:------------------------|
| 1 | Homepage Navigation | 1. Go to homepage <br> 2. Click on various categories | All links navigate correctly | All links worked as expected | Pass | No issues found |
| 2 | Search Functionality | 1. Go to homepage <br> 2. Enter "laptop" in the search bar <br> 3. Click search | List of laptops is displayed | List of laptops is displayed | Pass | Search is responsive |
| 3 | Invalid Search Query | 1. Go to homepage <br> 2. Enter "xyzabc123" in the search bar <br> 3. Click search | No results found message | "No results found" message displayed | Pass | Correct handling of invalid search |
| 4 | Product Page Details | 1. Click on a product from search results <br> 2. Check product details | Product details are displayed correctly | Product details displayed correctly | Pass | Images load quickly |
| 5 | Add to Cart | 1. Click on a product <br> 2. Click "Add to cart" | Product is added to cart | Product was added to cart | Pass | Cart updates correctly |
| 6 | Checkout Process | 1. Go to cart <br> 2. Click "Proceed to Checkout" <br> 3. Enter address and payment info | Order confirmation page is displayed | Order confirmation page displayed | Pass | Payment options available |
| 7 | User Registration | 1. Click "Sign Up" <br> 2. Fill in details <br> 3. Submit | Registration successful message | Registration successful message | Pass | Email verification received |
| 8 | Mobile Responsiveness | 1. Resize browser to mobile view <br> 2. Navigate through site | Site adjusts to mobile view | Site adjusts correctly | Pass | Mobile layout is user-friendly |
### Summary of Findings
#### 1. Major Issues Found
No significant issues were found during testing.
All key functionalities performed as expected.
#### 2. Usability Observations
The website navigation is intuitive and the search functionality is responsive.
Product pages provide comprehensive details enhancing user experience.
#### 3. Recommendations
Consider improving loading times for images on product pages to further enhance user experience.
Ensure that error messages for invalid inputs are clear and provide guidance for users.
#### 4. Overall Impression
The Jumia website is user-friendly and functions well across various tested features.
The testing revealed no critical bugs indicating a stable release.
### Conclusion
The exploratory testing of the Jumia website was successful; all major functionalities performing as intended. The site offers a positive user experience and no critical issues were identified.
Further testing could explore edge cases or additional functionalities not covered in this round.

[def]: https://www.jumia.co.ke/
[def2]: https://www.linkedin.com/in/fnjakai