/*
 HealthKit data is exclusive to iOS devices, meaning we cannot directly access it from other platforms or devices. To circumvent this limitation, we can create an iOS shortcut. This shortcut is designed to access HealthKit data on the user’s device. Once the data is accessed, the shortcut then uploads it to Firebase, a versatile cloud database that is accessible from any platform, including web apps.

 By storing the data in Firebase, we ensure that our web app can easily retrieve this data, allowing for seamless integration of health data across platforms. This method effectively bridges the gap between the iOS-exclusive HealthKit and cross-platform web applications, enabling a smooth flow of data from the user's iOS device to the web.
*/


#import <HealthKit/HealthKit.h>
#import <Firebase/Firebase.h>
HKHealthStore *healthStore = [[HKHealthStore alloc] init];
if ([HKHealthStore isHealthDataAvailable]) {
    NSSet *readTypes = [NSSet setWithObjects:[HKObjectType quantityTypeForIdentifier:HKQuantityTypeIdentifierStepCount], nil];
    
    [healthStore requestAuthorizationToShareTypes:nil readTypes:readTypes completion:^(BOOL success, NSError *error) {
        if (!success) {
            NSLog(@"You didn't get permission to access the health data.");
            return;
        }
        
        // Proceed to query HealthKit data here
    }];
}
HKSampleType *sampleType = [HKSampleType quantityTypeForIdentifier:HKQuantityTypeIdentifierStepCount];
NSPredicate *predicate = [HKQuery predicateForSamplesWithStartDate:startDate endDate:endDate options:HKQueryOptionStrictStartDate];

HKSampleQuery *sampleQuery = [[HKSampleQuery alloc] initWithSampleType:sampleType predicate:predicate limit:HKObjectQueryNoLimit sortDescriptors:@[sortByDate] resultsHandler:^(HKSampleQuery *query, NSArray *results, NSError *error) {
    if (!results) {
        NSLog(@"An error occurred fetching the user's steps: %@", error.localizedDescription);
        return;
    }
    
    // Process each sample and prepare for upload to Firebase
    NSMutableArray *dataToUpload = [[NSMutableArray alloc] init];
    for (HKQuantitySample *sample in results) {
        // Example: Collecting step count data
        double steps = [sample.quantity doubleValueForUnit:[HKUnit countUnit]];
        // Add your data to an array or dictionary to upload to Firebase
        [dataToUpload addObject:@{@"steps": @(steps), @"date": sample.startDate}];
    }
    
    // Dispatch to the main thread if you're updating the UI
    dispatch_async(dispatch_get_main_queue(), ^{
        // Update the UI or proceed to upload to Firebase
    });
    
    // Call your method to upload data to Firebase here
    [self uploadDataToFirebase:dataToUpload];
}];

[healthStore executeQuery:sampleQuery];
- (void)uploadDataToFirebase:(NSArray *)data {
    // Assuming you have a reference to your Firebase database
    FIRDatabaseReference *dbRef = [[FIRDatabase database] reference];
    
    for (NSDictionary *entry in data) {
        // Create a unique identifier for each entry, for example, using the date
        NSString *entryId = [NSString stringWithFormat:@"%@", entry[@"date"]];
        [[[dbRef child:@"healthData"] child:entryId] setValue:entry];
    }
}
